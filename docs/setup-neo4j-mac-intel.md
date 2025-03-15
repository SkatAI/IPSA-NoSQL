# **Setting Up Neo4j on macOS: Installation, Troubleshooting, and Importing Data**

## **🎯 Goal**
Neo4j is a powerful graph database, but setting it up manually on macOS can be tricky—especially when running it outside of Neo4j Desktop. My goal was to:

- **Manually install and run Neo4j** from the command line.
- **Manage databases** without relying on Neo4j Desktop.
- **Import a dump file** to load structured data into a new Neo4j database.
- **Run queries** using Cypher Shell instead of the browser.

This journey involved **multiple troubleshooting steps** to overcome missing dependencies, configuration issues, and licensing limitations.

---

## **🛠️ How I Set Up Neo4j**
Here’s how I got Neo4j running **without using Neo4j Desktop**.

### **1️⃣ Extract and Run Neo4j**
After downloading **Neo4j Enterprise Edition 5.24.0**, I extracted and started it manually:

```sh
cd ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/neo4j-enterprise-5.24.0
./bin/neo4j start
```

Neo4j started, but it **failed due to a missing Java Runtime**.

---

## **⚠️ Trouble: Java Runtime Issues**
Neo4j requires **Java 21**, but I only had **Java 17** installed. Running:

```sh
java -version
```
showed that my system was using Java 17.

---

## **✅ Fix: Install and Set Java 21**
I installed Java 21 using Homebrew:

```sh
brew install openjdk@21
```

Then, I set Neo4j to use Java 21 manually:

```sh
export JAVA_HOME="/opt/homebrew/opt/openjdk@21"
export PATH="$JAVA_HOME/bin:$PATH"
```

To make this **permanent**, I added it to `~/.zshrc`:

```sh
nano ~/.zshrc
```
and added:
```sh
export JAVA_HOME="/opt/homebrew/opt/openjdk@21"
export PATH="$JAVA_HOME/bin:$PATH"
```
Then, I applied the changes:
```sh
source ~/.zshrc
```

After this, Neo4j started successfully, but **authentication was required**.

---

## **⚠️ Trouble: Disable Authentication for Local Use**
Since this was just for **local testing**, I wanted to disable authentication.

---

## **✅ Fix: Disable Authentication in `neo4j.conf`**
I edited the configuration file:

```sh
nano ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/neo4j-enterprise-5.24.0/conf/neo4j.conf
```

And added:
```sh
server.auth.enabled=false
```

Then, I restarted Neo4j:
```sh
./bin/neo4j restart
```

Now, I could **connect to Neo4j without authentication**.

---

## **⚠️ Trouble: Neo4j License Expiration**
After starting Neo4j, I saw this warning:
```
This is a time-limited trial. You have 30 days remaining.
```
Neo4j **Enterprise Edition** requires a **license after 30 days**.

---

## **✅ Fix: Use Neo4j Community Edition**
To remove this limitation, I switched to **Neo4j Community Edition**, which is free and unlimited:

```sh
rm -rf ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/neo4j-enterprise-5.24.0
```

Then, I downloaded the **Community Edition** from:
🔗 [Neo4j Community Download](https://neo4j.com/download-center/#community)

Extracted and started it:
```sh
tar -xvzf neo4j-community-5.24.0-unix.tar.gz -C ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/
cd ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/neo4j-community-5.24.0
./bin/neo4j start
```

Now, Neo4j **worked without a time limit**.

---

## **⚠️ Trouble: Running Queries from the Command Line**
Neo4j was running, but I wanted to manage databases and run **Cypher queries from the terminal** instead of using the browser.

---

## **✅ Fix: Use Cypher Shell**
I accessed **Cypher Shell** to interact with Neo4j:
```sh
./bin/cypher-shell
```
Now, I could run queries like:
```cypher
SHOW DATABASES;
MATCH (n) RETURN n LIMIT 10;
```

I could also execute queries **directly from the terminal** without entering Cypher Shell:
```sh
cypher-shell -u neo4j -p mypassword "MATCH (n) RETURN n LIMIT 5;"
```

---

## **⚠️ Trouble: Importing a Dump File into a New Database**
I had a **Neo4j dump file (`neo4j-stackoverflow-50.dump`)** that I wanted to load into a **new database**.

---

## **✅ Fix: Import a Dump File into a New Database**
### **1️⃣ Stop the Database**
```sh
cypher-shell -u neo4j -p mypassword "STOP DATABASE mydatabase;"
```

### **2️⃣ Move the Dump File**
Neo4j only allows importing files from the **import/** directory:
```sh
mv /path/to/neo4j-stackoverflow-50.dump ~/Library/Application\ Support/Neo4j\ Desktop/Application/distributions/neo4j/neo4j-community-5.24.0/import/
```

### **3️⃣ Load the Dump File**
```sh
./bin/neo4j-admin database load mydatabase --from=import/neo4j-stackoverflow-50.dump --force
```

### **4️⃣ Start the Database**
```sh
cypher-shell -u neo4j -p mypassword "START DATABASE mydatabase;"
```

### **5️⃣ Verify the Import**
```sh
cypher-shell -u neo4j -p mypassword "MATCH (n) RETURN n LIMIT 10;"
```

Now, the **Stack Overflow dataset was successfully loaded** into Neo4j.

---

## **🚀 Final Thoughts**
This journey of setting up Neo4j **without Neo4j Desktop** had multiple challenges:
- **Java version conflicts** → Fixed by installing **Java 21**.
- **Authentication issues** → Disabled for **local development**.
- **Trial license expiration** → Switched to **Community Edition**.
- **Cypher queries from CLI** → Used **Cypher Shell**.
- **Importing a dump file** → Used `neo4j-admin database load`.

By overcoming these, I now have **full control over Neo4j via the terminal**, allowing me to manage databases and execute queries **without relying on Neo4j Desktop**.

---

### **Did this guide help?**
If you're setting up Neo4j on **macOS** and facing similar issues, feel free to share your experience or ask questions! 🚀

---

This article summarizes your session in a clear and structured way, making it **perfect for posting online**! Let me know if you’d like any tweaks. 😊