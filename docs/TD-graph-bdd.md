# TD graph bdd

Il y a plusieurs offres de graph databases https://db-engines.com/en/ranking/graph+dbms

voir aussi https://www.marktechpost.com/2024/06/03/top-open-source-graph-databases/


- neo4j est le leader du marché

Mais il y a de nombreux concurrents


- tigergraph
- arangodb
- OrientDB
- Aerospike Graph
- etc etc


certains de ces database sont multi-modeles :  graph et documents

Le but de l'exercice est de trouver des alternatives à neo4j

Vous allez dans un premier temps tester Neo4j

Puis choisir une autre bdd graph et comparer

Vous documenterez votre methode, resultats et conclusions.

## Scenario

Vous etes CTO d'une petite entreprise de conseil en l'analyse de données.

Un nouveau projet d'analyse de reseau vient d'être signé par l'equipe commerciale, mais vous n'avez ni les données ni les détails du projet.

Il vous faut choisir la bonne base de données de type graph.

Neo4j est le leader du marché des graph bdd. Mais il y a de nombreuses alternatives.

Votre but tester les alternatives a Neo4j pour faire le bon choix

Vous vous ferez une opinion sur les aspects techniques

- la rapidité de prise en main
- les capacité d'analyse des données
- performance sur l'import et l'execution de requetes complexes
- compatibilté avec les data store et outils existant (AWS ou GCP cloud) : Integration: APIs, connectors to your existing data pipeline. par exemple possibilité de connection dans un Colab notebbook, compatibilité avec des langages standard (python, javascript)
  - GraphQL

et sur les aspects couts et support

- la qualité de la documentation et la fraicheur des tutoriaux et resources en ligne
- ce qui est compris dans l'offre gratuite / communauté par rapport à la version payante entreprise
- l'ecosysteme : services hosté cloud,
- les prix pour l'offre entreprise
- le pays d'origine de la bdd
- licenses


Pour cela vous allez

- installer la bdd en local
- importer un dataset
- explorer les données. Notamment  trouver les influencers (degree, inbetweeness), les chemins courts (DJikstra) et detecter  les communautes (Louvain)


datasets de tests: ceux que vous avez utilisés pour mongoDB

ou bien :
- paris transport au format GTFS
- star wars au format csv et autres dataset dans ce meme github repo

Vous aurez surement a transformer les données dans un format compatible pour l'import dans la bdd graph.

Cette étape est un des points important de l'evaluation.


Vous pourrez aussi regarder les points suivants s'ils vous semblent iomportant ou particulierement relevant pour la bdd en question

- Sécurité et contrôle d'accès : Comment ces bases de données gèrent les permissions
- Maintenance et sauvegarde : Processus de backup et restauration
- Visualisation native : Comparer les outils de visualisation intégrés
- Écosystème d'extensions : Explorer les plugins et extensions disponibles


# Livrable

un document google doc avec vos resultats et conclusions

