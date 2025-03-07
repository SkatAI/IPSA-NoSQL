# RAG Search Application

This project is a Streamlit interface for Retrieval-Augmented Generation (RAG) that:

- Connects to a MongoDB database
- Uses a collection of texts and their embeddings for retrieval
- Provides a simple search interface for natural language queries

## Features

- **Simple Search Interface**: A clean page with a search bar for text queries
- **Vector Similarity Search**: Queries are embedded and compared to document embeddings
- **Relevant Results Display**: Search results are shown ranked by relevance

## How It Works

When the user submits a query:

1. The query is embedded using SentenceTransformer
2. The embeddings are searched in the MongoDB database
3. The most relevant documents are retrieved and displayed to the user

## Embeddings

We use the sentence transformers library with the model `paraphrase-multilingual-MiniLM-L12-v2` for embedding the queries.

## Docker Setup

This project uses Docker to avoid installing dependencies locally.

### Prerequisites

- Docker and Docker Compose installed on your machine
- MongoDB Atlas account with vector search capability
- MongoDB collection with document texts and their embeddings

### Setup Instructions

1. Clone this repository

2. Create a `.env` file based on the `.env.example` template:
   ```
   cp .env.example .env
   ```

3. Update the `.env` file with your MongoDB connection details:
   ```
   MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/?retryWrites=true&w=majority
   MONGODB_DB=your_database_name
   MONGODB_COLLECTION=your_collection_name
   ```

4. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

5. Access the application in your browser at:
   ```
   http://localhost:8501
   ```

### MongoDB Collection Structure

Your MongoDB collection should have documents with at least these fields:
- `text`: The document content
- `embedding`: Vector embedding of the document (array of floats)

### Vector Search Index

Make sure you have created a vector search index in your MongoDB Atlas collection named `vector_index` on the `embedding` field.

## Development

If you want to modify the application:

1. Make changes to the `app.py` file
2. The changes will be automatically reflected in the running container (thanks to the volume mount)

