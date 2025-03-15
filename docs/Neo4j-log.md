# Neo4j



Running neo4j on local and trying to import a simple dataset


- with the desktop

after creatrng a new database
many problems with
- ports
- settings
- locating settings conf file on my machine
- having to install java v21 (neo4j desktop comes with v17)

should have tried Docker

In the end managed to install neo4j on local, manually,

I can run cypher-shell, neo4j and neo4j admin

disabled the authentication in the conf file



# found datasets

found a few datasets online that seemd real nice
for instance
https://github.com/neo4j-graph-examples/star-wars/tree/main

Using LOAD CSV in cypher shell

must move the csv files into a /import folder where the neo4j is installed

then strugled with having to stop / start neo4j
creating a database
syntax problems in the neo4j-admin statement

neo4j-admin database import full starwars --verbose --overwrite-destination --multiline-fields=true --nodes Character=starwars.nodes.Character.csv, starwars.nodes.Film.csv \
    --relationships=APPEARED_IN=starwars.relationships.APPEARED_IN.csv

 import doc is ok but lacks examples


 then finally ,  error

 (global id space)-[APPEARED_IN]->0 (global id space) referring to missing node APPEARED_IN


 The repo is for version 4, I have version 5.24 rtunning on local. that does not help


 # other imports

if we want to import csv they have to be in a very specific format

not possible to infr the schema from the csv files

also need to separate nodes, and relations in different csv files

JSON is probably similar in specification


There are other formats
but they seem to require specific externa modules
for instance
GTFS: transport requires https://github.com/skjolber/gtfs-neo4j-import
Converts GTFS ZIP files to CSV files importable to Neo4j.

surely doable but probably time consuming


# Bingo

The I stumbled unto the demo server
hallelujah I was saved

https://neo4j.com/docs/getting-started/appendix/example-data/

twitter : https://demo.neo4jlabs.com:7473/browser/?dbms=neo4j://twitter@demo.neo4jlabs.com&db=twitter
stacckoverflow : https://demo.neo4jlabs.com:7473/browser/?dbms=neo4j://stackoverflow@demo.neo4jlabs.com&db=stackoverflow


requires a password : which is the database name !

but the databases are big

41,782,536 posts on stackoverflow, 16,389,567 questions, 8,917,507 users

takes forever to run a simple query

2407 tweets, and 38986 users

probably an extract of all tweets by neo4j


# and still unable to use Graph data science

In the meantime, networkx has a lot of data science analysis algorithms and tools. more than neo4j

so why use neo4j to do the analysis
It seems possible to connect a networkx graph in python to a neo4j instance to source the data


Running GDS on the demo server is not recommended if at all possible!

# ETL

it looks possible to connect to postgres with a valid JDBC driver

but there also that requires to write a schema mapping file



# Conclusion

Neo4j seems like a promess that has not delivered

it's very cool on paper

but most repos, datasets, and tools are old
and often not compatible with version 5

also neo4j is based on java, which adds to the setup pain

there's probably a good way to install eveything, most probably on a hosted service solution

but I would definitely not use neo4j for now

In short why use the database ot do the analysis
what seemed like a good idea and an advantage of neo4j with GDS ends up being meh
database : store the data
analysis is external

In real projects I would

- store the data in SQL or Document store
- export the data, format it as network and then do the analysis

# Alternatives to neo4j

- tigergraph
- arangodb













in teh end able to import nodes but relations give a syntax error
