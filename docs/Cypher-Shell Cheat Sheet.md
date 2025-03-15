# **Cypher-Shell Cheat Sheet** 🚀

### **1️⃣ Connect to a Neo4j Database**
```sh
cypher-shell -u neo4j -p your_password
```
or if running on a remote server:
```sh
cypher-shell -a bolt://your_server_ip:7687 -u neo4j -p your_password
```
---

### **2️⃣ Create a New Database (Neo4j Enterprise)**
```cypher
CREATE DATABASE myDatabase;
```
🔹 **Check Available Databases:**
```cypher
SHOW DATABASES;
```
🔹 **Switch to a Database:**
```cypher
:use myDatabase
```
---

### **3️⃣ Explore an Existing Database**
🔹 **List All Nodes:**
```cypher
MATCH (n) RETURN n LIMIT 10;
```
🔹 **Check Schema (Labels, Relationships, Indexes):**
```cypher
CALL db.schema.visualization;
```
🔹 **List All Labels:**
```cypher
CALL db.labels;
```
🔹 **List All Relationship Types:**
```cypher
CALL db.relationshipTypes;
```
🔹 **List All Property Keys:**
```cypher
CALL db.propertyKeys;
```
---

### **4️⃣ Querying Data**
🔹 **Find Nodes by Label:**
```cypher
MATCH (p:Person) RETURN p LIMIT 5;
```
🔹 **Find Relationships:**
```cypher
MATCH (a)-[r]->(b) RETURN a, r, b LIMIT 10;
```
🔹 **Count Nodes by Label:**
```cypher
MATCH (n:Person) RETURN count(n);
```
---

### **5️⃣ Managing Indexes**
🔹 **Create an Index for Faster Queries:**
```cypher
CREATE INDEX FOR (p:Person) ON (p.name);
```
🔹 **Show Existing Indexes:**
```cypher
SHOW INDEXES;
```
🔹 **Drop an Index:**
```cypher
DROP INDEX myIndexName;
```
---

### **6️⃣ Exiting Cypher-Shell**
```sh
:exit
```

🔥 **Tip:** Use **Tab completion** for quick command suggestions inside `cypher-shell`! 🚀