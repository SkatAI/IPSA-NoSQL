import streamlit as st
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="RAG Search App",
    page_icon="🔍",
    layout="wide"
)

# Initialize the embedding model
@st.cache_resource
def load_embedding_model():
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Connect to MongoDB
@st.cache_resource
def connect_to_mongodb():
    # MongoDB connection string from environment variable
    uri = os.environ.get("MONGODB_URI")
    if not uri:
        st.error("MongoDB URI not found. Please set the MONGODB_URI environment variable.")
        return None
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    # Get database and collection names from environment variables or use defaults
    db_name = os.environ.get("MONGODB_DB", "rag_database")
    collection_name = os.environ.get("MONGODB_COLLECTION", "documents")
    
    # Connect to the database and collection
    db = client[db_name]
    collection = db[collection_name]
    
    # Test connection
    try:
        client.admin.command('ping')
        st.sidebar.success("Connected to MongoDB!")
        return collection
    except Exception as e:
        st.sidebar.error(f"Failed to connect to MongoDB: {e}")
        return None

def search_similar_documents(collection, query_embedding, limit=5):
    """Search for documents similar to the query embedding."""
    # Convert numpy array to list for MongoDB
    query_embedding_list = query_embedding.tolist()
    
    # Perform vector search using $vectorSearch (MongoDB Atlas)
    try:
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "queryVector": query_embedding_list,
                    "path": "embedding",
                    "numCandidates": 100,
                    "limit": limit
                }
            },
            {
                "$project": {
                    "text": 1,
                    "score": {"$meta": "vectorSearchScore"},
                    "_id": 0
                }
            }
        ]
        
        results = list(collection.aggregate(pipeline))
        return results
    except Exception as e:
        st.error(f"Error performing vector search: {e}")
        
        # Fallback to manual search if vectorSearch is not available
        st.warning("Falling back to manual similarity search")
        
        # Get all documents
        documents = list(collection.find({}, {"text": 1, "embedding": 1, "_id": 0}))
        
        # Calculate cosine similarity manually
        similarities = []
        for doc in documents:
            if "embedding" in doc:
                doc_embedding = np.array(doc["embedding"])
                similarity = np.dot(query_embedding, doc_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
                )
                similarities.append((doc["text"], similarity))
        
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Format results similar to vectorSearch
        results = [{"text": text, "score": float(score)} for text, score in similarities[:limit]]
        return results

def main():
    st.title("🔍 RAG Search Application")
    st.markdown("Search for relevant documents using natural language queries.")
    
    # Initialize components
    model = load_embedding_model()
    collection = connect_to_mongodb()
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This application uses:
        - MongoDB for document storage
        - SentenceTransformer for embedding queries
        - Vector search for finding relevant documents
        """)
    
    # Search interface
    query = st.text_input("Enter your query:", placeholder="What would you like to search for?")
    
    # Search button
    search_button = st.button("Search")
    
    # Process search when button is clicked
    if search_button and query and collection:
        with st.spinner("Processing your query..."):
            # Embed the query
            query_embedding = model.encode(query)
            
            # Search for similar documents
            results = search_similar_documents(collection, query_embedding)
            
            # Display results
            if results:
                st.subheader("Search Results")
                
                for i, result in enumerate(results):
                    with st.container():
                        st.markdown(f"### Result {i+1} (Score: {result['score']:.4f})")
                        st.markdown(result["text"])
                        st.divider()
            else:
                st.info("No matching documents found. Try a different query.")
    
    elif search_button and not query:
        st.warning("Please enter a query to search.")

if __name__ == "__main__":
    main()
