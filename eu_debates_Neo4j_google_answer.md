# EU parsing and debate verbatim for Neo4j

see intro of
https://political-llm.org/

    LLMs have been critical in analyzing extensive corpora of political texts, encompassing a wide range of sources such as political speeches, legislative documents, social media content, and news articles


## inference

using a record of past EU debates
can I simulate the contribution of a MEP on potential future debates ?
and can I measure how the actual contribution differs from the actual expected  one ?
Would that be a proxy for discourse evolution ?
how is the individual MEP contribution diverging from the political stance
https://arxiv.org/abs/2303.12057

## Google AI studio Session
see https://aistudio.google.com/prompts/101Z13yRkwI3WWrKd_4T_UYn8fQKJmY87

All the debates are publicly accessible. I have a large dataset of such debates verbatim.
I am teaching a course on Neo4J
I would like to use these debates as a demo and hands-on exercises
think about the questions that could be asked to analyse such debates by jourrnalists or political analysts

- What type of graph model could I infer from these debates in  terms of nodes, relationahips, labels and properties



Okay, that's a fantastic idea for a Neo4j course! Using political debates as a practical example will be highly engaging and relevant. Let's explore a graph model suitable for this purpose, keeping in mind the types of questions a journalist or political analyst might ask.

**Graph Model for Political Debates**

Here's a proposed graph model, outlining nodes, relationships, labels, and properties:

**1. Nodes (Entities):**

*   **`Speaker`:** Represents an individual participant in the debate.
    *   **Labels:** `Speaker`, `Person`, `Politician`
    *   **Properties:**
        *   `speaker_id`: Unique identifier (e.g., a numeric ID or a string).
        *   `name`: Full name of the speaker.
        *   `political_group`: The political group/party they belong to.
        *   `country`: Country they represent.
        *   `role`: e.g., MEP, Commissioner, etc.
*   **`Debate`:** Represents a specific debate event.
    *   **Labels:** `Debate`, `Event`
    *   **Properties:**
        *   `debate_id`: Unique ID for the debate.
        *   `date`: Date of the debate.
        *   `title`: Title or subject of the debate.
        *   `venue`: Location of the debate (e.g., "Strasbourg").
*   **`Argument`:** Represents a specific claim or point made during the debate.
    *   **Labels:** `Argument`, `Claim`
    *   **Properties:**
        *   `argument_id`: Unique identifier for the argument.
        *   `text`: The actual text of the argument.
        *   `sentiment`: (Optional) Sentiment analysis result (e.g., "positive," "negative," "neutral").
*   **`Topic`:** Represents a general theme or issue discussed in the debate.
    *   **Labels:** `Topic`, `Issue`
    *   **Properties:**
        *   `topic_id`: Unique ID for the topic.
        *   `name`: Name of the topic (e.g., "Energy Poverty," "Green Deal," "Nuclear Energy").
*  **`Organization`:** Represents a political entity, organization or company involved in the debate.
     * **Labels:** `Organization`, `PoliticalEntity`
     * **Properties:**
          * `org_id`: Unique ID
          * `name`: Name of the organization (e.g., Greenpeace, European Comission).
          * `type`: Type of organization (e.g., NGO, Political Party, International Organization).

**2. Relationships (Interactions):**

*   **`(Speaker)-[:PARTICIPATED_IN]->(Debate)`:**  A speaker participated in a particular debate.
*   **`(Speaker)-[:MAKES]->(Argument)`:**  A speaker made a specific argument.
*   **`(Argument)-[:DISCUSSES]->(Topic)`:**  An argument relates to a particular topic.
*   **`(Speaker)-[:BELONGS_TO]->(PoliticalGroup)`:**  A speaker belongs to a political group
*   **`(Speaker)-[:REPRESENTS]->(Country)`:** A speaker represents a particular country.
*   **`(Argument)-[:REFERENCES]->(Organization)`:** An argument references a specific organization.
*   **`(Organization)-[:HAS_POSITION_ON]->(Topic)`:** An Organization has a position on a specific topic.
*   **`(Argument)-[:OPPOSES]->(Argument)`:** An argument is in opposition to another.
*   **`(Speaker)-[:SIMILAR_TO]-(Speaker)`:** Speakers share similar opinions or vote patterns. *(Optional for more complex analysis).*

**3. Relationship Properties:**

*   **`[:MAKES]`:**
    *   `order_in_debate` The order in which the speaker made the argument.

**Questions for Analysis (Neo4j Cypher Queries)**

Here are some example questions and how they translate to Neo4j Cypher queries.

*   **Topic-Based Questions**
    *   **Q1: "Which speakers discussed the topic of 'Energy Poverty'?"**
        ```cypher
        MATCH (t:Topic {name: 'Energy Poverty'})<-[:DISCUSSES]-(a:Argument)<-[:MAKES]-(s:Speaker)
        RETURN s.name, s.political_group
        ```
    *   **Q2: "What are the main arguments related to the 'Green Deal' topic?"**
        ```cypher
        MATCH (t:Topic {name: 'Green Deal'})<-[:DISCUSSES]-(a:Argument)
        RETURN a.text
        ```
*   **Speaker-Based Questions:**
    *   **Q3: "What arguments did 'Kadri Simson' make during her speech?"**
        ```cypher
        MATCH (s:Speaker {name: 'Kadri Simson'})-[:MAKES]->(a:Argument)
        RETURN a.text
        ```
    *   **Q4: "Which other debates did 'Beata Szydło' participate in?"**
        ```cypher
        MATCH (s:Speaker {name: 'Beata Szydło'})-[:PARTICIPATED_IN]->(d:Debate)
        RETURN d.title, d.date
        ```
   *   **Q5: "Which speakers share similar opinions regarding nuclear energy?"**
        ```cypher
       MATCH (s1:Speaker)-[:MAKES]->(arg1:Argument)-[:DISCUSSES]->(t:Topic {name: 'Nuclear Energy'})
        WITH s1, arg1
        MATCH (s2:Speaker)-[:MAKES]->(arg2:Argument)-[:DISCUSSES]->(t)
        WHERE s1 <> s2 AND arg1.sentiment = arg2.sentiment
        RETURN s1.name, s2.name, arg1.sentiment;
        ```
*   **Political Group Analysis:**
    *   **Q6: "What are the most common topics discussed by the 'PPE' political group?"**
        ```cypher
        MATCH (s:Speaker)-[:BELONGS_TO]->(pg:PoliticalGroup {name: 'PPE'})-[:MAKES]->(a:Argument)-[:DISCUSSES]->(t:Topic)
        RETURN t.name, count(t) ORDER BY count(t) DESC
        ```
    *   **Q7: "How does the S&D group’s arguments on the 'Green Deal' compare to the ECR group’s?"**
        ```cypher
        MATCH (pg1:PoliticalGroup {name: 'S&D'})<-[:BELONGS_TO]-(s1:Speaker)-[:MAKES]->(a1:Argument)-[:DISCUSSES]->(t:Topic {name: 'Green Deal'})
        WITH a1, t
        MATCH (pg2:PoliticalGroup {name: 'ECR'})<-[:BELONGS_TO]-(s2:Speaker)-[:MAKES]->(a2:Argument)-[:DISCUSSES]->(t)
        RETURN pg1.name, a1.text as SD_Arguments, pg2.name, a2.text AS ECR_arguments
        ```
*   **Debate-Specific Questions:**
    *   **Q8: "Which topics were discussed in the debate on 'Rise of energy prices and fighting energy poverty'?"**
         ```cypher
         MATCH (d:Debate {title: 'Rise of energy prices and fighting energy poverty (debate)'})<-[:PARTICIPATED_IN]-(s:Speaker)-[:MAKES]->(a:Argument)-[:DISCUSSES]->(t:Topic)
         RETURN DISTINCT t.name
        ```
    *   **Q9: "What was the order of speeches during the debate?"**
          ```cypher
          MATCH (d:Debate {title: 'Rise of energy prices and fighting energy poverty (debate)'})<-[:PARTICIPATED_IN]-(s:Speaker)-[:MAKES]->(a:Argument)
          RETURN s.name, a.order_in_debate ORDER BY a.order_in_debate
          ```

*  **Organization Analysis**

     *   **Q10: "What was the position of Greenpeace regarding nuclear energy?"**
      ```cypher
        MATCH (o:Organization {name: 'Greenpeace'})-[:HAS_POSITION_ON]->(t:Topic {name: 'Nuclear Energy'})
        RETURN o, t
      ```
     *   **Q11: "Which organizations were cited in arguments related to the 'Green Deal' topic?"**
        ```cypher
        MATCH (t:Topic {name: 'Green Deal'})<-[:DISCUSSES]-(a:Argument)-[:REFERENCES]->(o:Organization)
        RETURN DISTINCT o.name
        ```

**Key Considerations for Your Course:**

*   **Data Cleaning and Preparation:** The debates might require text processing, such as cleaning HTML tags, splitting speakers, and argument extraction. Sentiment analysis will add another layer of complexity.
*   **Importing Data:** Plan how you will import this data into Neo4j (e.g., CSV, JSON, custom importers).
*   **Progressive Learning:** Begin with basic queries and then introduce more complex ones.
*   **Visualization:** Use Neo4j Browser or Bloom to visualize the graph and the results of the queries.
*   **Real-World Relevance:** Connect the queries to the types of questions that journalists, political analysts, or policy researchers might ask.
*   **Optional Extensions:** You can expand the model with aspects like specific policies, references to other documents, or sentiment analysis results of statements.

Let me know if you want more specific queries, suggestions, or how to go about the import process.
