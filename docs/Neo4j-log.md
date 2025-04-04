# A quick graph data science demo on Neo4j


This title is what I had in mind for my next class on the Neo4j graph database.

We had done the neo4j tutorials on Auradb and I was looking forward to diving into community detection and shortest path finding with a cool dataset hosted on Neo4j.

I set out to build a cool demo early morning on a Thursday for the course on the next day. I had the whole day to myself. What could go wrong ?

Since AuraDb does not include the graph data science module I had to run Neo4j on my local Intel Mac.

The plan:  Run neo4j on local, import a simple dataset and demo some cool graph data science. Even look into LLM driven graph knowledge. Fun stuff.



# Neo4j Desktop

Since the neo4j desktop is available for download why not start with that.
Download, launch, find a dump of the stackoverflow dataset.

Okk the UI is confusing. But it's a matter of getting used to it.
I manage to create a project, a database, and I start the database.
I add a dataset. A neo4j dump. So it should work.

Then the problem starts. Some recurring port mapping errors. The pop ups do not solve the issue. I find the neo4j config file, somewhere in the Mac, change the ports, ... relaunch ... ah some other error pops up. weird stuff. No clue how to fix it. Neither do my army of loyal assistants (ChatGPT, Gemini, Mistral, Deepseek or Claude).

ok out with the neo4j desktop, in with the local install. I always work better with the command line.
I find where everything is installed.

But I have to install java21, the browser came with java 17. ok I reinstall java. always scary java.


At this point I really should have gone the Docker way. Never trust the UI app, always choose Docker.

In the end I managed to install neo4j on local, manually,

I can run cypher-shell, neo4j and neo4j admin

I even disabled the authentication in the conf file. Since it's all local demo stuff.



# Found datasets

I look online and quickly find a great repo of multiple neo4j datasets : https://github.com/neo4j-graph-examples

Skimming through the list, the star wars dataset catches my attention.  It has all the ships, characters, planets depicted in the movies. A fun dataset to work with. Engaging for my students. Let's go.

https://github.com/neo4j-graph-examples/star-wars/tree/main

I plan on Using `LOAD CSV` in cypher shell

oh. But first I must move the csv files into the `/import` folder where the neo4j is installed

Where is neo4j installed ? I found it already but can't remember the path. Got it. On my mac it's something like this

/Users/alexis/Library/Application Support/Neo4j Desktop/Application/distributions/neo4j/neo4j-enterprise-5.24.0/

ah a path that contains spaces, always painful in the terminal.

My assistant tells me this is the command I should use.
neo4j-admin database import full starwars --verbose --overwrite-destination --multiline-fields=true --nodes Character=starwars.nodes.Character.csv, starwars.nodes.Film.csv \
    --relationships=APPEARED_IN=starwars.relationships.APPEARED_IN.csv

I admit having read the documentation at this point on how to import a csv file of nodes or relations with `neo4j-admin`.
Hence the `--overwrite-destination --multiline-fields=true` flags that allow to overwrite the existing database and allow for columns with multiple lines in the csv file. (csv should not be the format in that case. just sayin')

So I try this command several times, and each time I need to start and stop the neo4j process. Which takes a lot of time. precious time. It's already late in the morning. And I haven't started yet.

I finally manage to import the nodes for the characters and the movies.



But when it comes to importing relationships, error!

```shell
(global id space)-[APPEARED_IN]->0 (global id space) referring to missing node APPEARED_IN
```

At this point I notice that the dataset specifies a neo4j version 4 and I have 5.4. I doubt that is the cause of the error above. But at this point I feel less and less confident about my ... confidence.

Since time is flying, and I don';t want to start digging into the csv file itself, I give up on that dataset.

I long for my beloved postgresql who would never cause me such pains. I fondly remember importing barrels of csv files in a single command line without ever having to restart the database. Even mongoimport behaves better.

The problem with importing csv data into a neo4j database with neo4j-admin is multiple
- impossible to infer the schema from the csv
- need to stop the server
- need to break down the nodes and the relationships in separate files.

Not very user friendly.

I confess I did not try to import JSON files which may have provided for a smoother, gentler experience. who knows.

# other imports

Trapped as I was, I began frantically searching for other datasets in other formats.

The GTFS format is well suited for transport data. Transportation networks are perfect for graph analysis. It's a perfect match.
and there's even a GTFS to neo4j import library. I am saved. The students are saved. My teaching career will know no bounds! World oyster etc

ah! "The project is implemented in Java and built using Maven" ouch. and the repo saw last updated ... 7 years ago.
In the readme is a [link](https://blog.bruggen.com/2015/11/loading-general-transport-feed-spec.html) to a blog post on import GTFS in Neo4j... ouch it's from 2015.

Ok so the lib probably does not work with neo4j 5.4. Not even going to try. Surely doable but probably time consuming


# Bingo

I search and search for other datasets. I only find old deprecated libraires and repos. until ... What is that ... the dataset page on the neo4j web site ? Might they have a dataset I can use ?


https://neo4j.com/docs/getting-started/appendix/example-data/

And yes not only do they have the dataset but also a link to a demo server. Oh joy!


twitter : https://demo.neo4jlabs.com:7473/browser/?dbms=neo4j://twitter@demo.neo4jlabs.com&db=twitter
stackoverflow : https://demo.neo4jlabs.com:7473/browser/?dbms=neo4j://stackoverflow@demo.neo4jlabs.com&db=stackoverflow

I click and the neo4j browser appears. All I need now is to connect to the server... but there's a password needed. I do not know the password! Is it Abracadabra ? no
At this point I feel I'm a badass hacker and guess the password in only 3 tries. The password is the same as the database name.



The stackoverflow  database happens to be rather large with 41.7M posts, 16.5M questions and 9M users. So every query takes absolutely forever to run. No chance I can dream of calculating degrees, and inbetweenness. and anyway there's no Data science graph available so no shortest path algo or community detection.

The twitter dataset is smaller (2407 tweets). It seems to be consisting of tweets (remember tweets, ah sweet nostalgia) written by the neo4j account. Not great for community detection.



# Networkx

In the meantime, Networkx has a lot more data science analysis algorithms and tools than Neo4j. So why use neo4j to do the analysis?

It seems possible to connect a Networkx graph in python to a neo4j instance to source the data with a valid JDBC driver.

Another option would be the excellent and powerful Gephi library which offers fantastic graph visualizations.

# Conclusion

In this short time, trying to build a simple graph demo with some cool dataset, I was not able to get anything done.

The Neo4j tutorials on Aura are well designed and informative. The northwind dataset is complex enough, the stack overflow has potential and the Pole data is fun to play with. But AuraDB in its free version does not include the Graph data science module.

My overall feeling is that Neo4j is a promise that has not delivered

Neo4j is very cool on paper (Panama project)  or in linkedin posts on LLM driven knowledge graphs, but many repos, datasets, and tools are old, deprecated, and often not compatible with version 5. Neo4j is also based on java, which adds to the setup pain. At least on Mac.

There's surely a proper way to install everything, most probably on a hosted service solution.  And I definitely should have started with the Docker version instead of installing the Neo4j Browser. Never trust the UI app, always choose Docker.

In the end, the promise of doing the analysis with the same tech as the data hosting does not really make sense. The analysis tools are less developed than the ones in Gephi or Networkx.

If I had to do some network analysis or build a knowledge graph I would

store the data in Postgresql or maybe Mongodb.
Then write some extraction script that formats the data as a graph dataset
and finally do the analysis in a dedicated tool like Gephi or using a library such as Networkx.

In real projects I would

- store the data in SQL or Document store
- export the data, format it as network and then do the analysis

# Alternatives to Neo4j

Neo4j is not the only graph database out there. And I have yet to test the alternatives like tigergraph, arangodb, Dgraph …

Looking back, I was stressed and short on time and that did not help. Things would have turned out better If I had taken the time to be more thorough. I have worked for years with PostgreSQL and the comparison may not have helped. Neo4j is not as developed or robust as standard SQL databases.
But looking back at all the neo4j online  resources, blogs, libs, ... I have stumbled upon during this experiment, it feels as if there is a popularity cycle to neo4j.
New excitement or use cases arise over graph databases, things get built and then the enthusiasm dies down and these  resources get stale. Until the next wave of excitement. Like LLM based knowledge graphs.

Long Live SQL! Long Live PostgreSQL!

