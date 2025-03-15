/Users/alexis/work/references/datasets/star-wars/import


neo4j-admin database import full --nodes import/movies_header.csv,import/movies.csv \
--nodes import/actors_header.csv,import/actors.csv \
--relationships import/roles_header.csv,import/roles.csv



neo4j-admin database import full --nodes Character=starwars.nodes.Character.csv, starwars.nodes.Film.csv \
    --relationships=APPEARED_IN=starwars.relationships.APPEARED_IN.csv \
    starwars


neo4j-admin import \
--nodes=Character=starwars.nodes.Character.csv \
--nodes=Film=starwars.nodes.Film.csv \
--nodes=Planet=starwars.nodes.Planet.csv \
--nodes=Species=starwars.nodes.Species.csv \
--nodes=Starship=starwars.nodes.Starship.csv \
--nodes=Vehicle=starwars.nodes.Vehicle.csv \
--relationships=APPEARED_IN=starwars.relationships.APPEARED_IN.csv \
--relationships=HOMEWORLD=starwars.relationships.HOMEWORLD.csv \
--relationships=OF=starwars.relationships.OF.csv \
--relationships=PILOT=starwars.relationships.PILOT.csv




LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Film.csv' AS row
CREATE (:Film {
    id: toInteger(row.`:ID`),
    producer: row.producer,
    title: row.title,
    release_date: row.release_date,
    created: row.created,
    director: row.director,
    opening_crawl: row.opening_crawl,
    episode_id: toInteger(row.`episode_id:long`),
    edited: row.edited,
    url: row.url
});




LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Character.csv' AS row
CREATE (:Character {
    id: toInteger(row.ID),
    name: row.name,
    birth_year: row.birth_year,
    eye_color: row.eye_color,
    height: toInteger(row.height),
    gender: row.gender,
    skin_color: row.skin_color
});





---

### **Films**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Film.csv' AS row
CREATE (:Film {
    id: toInteger(row.ID),
    title: row.title,
    episode_id: toInteger(row.episode_id),
    release_date: row.release_date
});
```

---

### **Planets**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Planet.csv' AS row
CREATE (:Planet {
    id: toInteger(row.ID),
    name: row.name,
    climate: row.climate,
    terrain: row.terrain,
    population: toInteger(row.population)
});
```

---

### **Species**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Species.csv' AS row
CREATE (:Species {
    id: toInteger(row.ID),
    name: row.name,
    classification: row.classification,
    language: row.language
});
```

---

### **Starships**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Starship.csv' AS row
CREATE (:Starship {
    id: toInteger(row.ID),
    name: row.name,
    model: row.model,
    manufacturer: row.manufacturer,
    length: toFloat(row.length),
    hyperdrive_rating: toFloat(row.hyperdrive_rating)
});
```

---

### **Vehicles**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.nodes.Vehicle.csv' AS row
CREATE (:Vehicle {
    id: toInteger(row.ID),
    name: row.name,
    model: row.model,
    manufacturer: row.manufacturer,
    length: toFloat(row.length),
    vehicle_class: row.vehicle_class
});
```

---

## **2️⃣ Create Relationships**

### **Character APPEARED_IN Film**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.relationships.APPEARED_IN.csv' AS row
MATCH (c:Character {id: toInteger(row.START_ID)}), (f:Film {id: toInteger(row.END_ID)})
CREATE (c)-[:APPEARED_IN]->(f);
```

---

### **Character HOMEWORLD Planet**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.relationships.HOMEWORLD.csv' AS row
MATCH (c:Character {id: toInteger(row.START_ID)}), (p:Planet {id: toInteger(row.END_ID)})
CREATE (c)-[:HOMEWORLD]->(p);
```

---

### **Character OF Species**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.relationships.OF.csv' AS row
MATCH (c:Character {id: toInteger(row.START_ID)}), (s:Species {id: toInteger(row.END_ID)})
CREATE (c)-[:OF]->(s);
```

---

### **Character PILOT Starship**
```cypher
LOAD CSV WITH HEADERS FROM 'file:///starwars.relationships.PILOT.csv' AS row
MATCH (c:Character {id: toInteger(row.:START_ID)}), (s:Starship {id: toInteger(row.:END_ID)})
CREATE (c)-[:PILOT]->(s);
```

---

## **3️⃣ Verify Data Import**
Once you've executed these queries, you can check the imported data with:

```cypher
MATCH (n) RETURN n LIMIT 10;
MATCH (c:Character)-[r]->(f:Film) RETURN c, r, f LIMIT 10;
```

---

### **⚡ Next Steps**
- **Indexing:** Improve query performance by creating indexes.
```cypher
CREATE INDEX FOR (c:Character) ON (c.id);
CREATE INDEX FOR (f:Film) ON (f.id);
```
- **Visualization:** Use Neo4j Browser to visualize graph relationships.

🚀 **Now you're ready to explore the Star Wars graph dataset!** Let me know if you need any modifications!