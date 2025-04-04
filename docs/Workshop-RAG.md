# TP Workshop RAG

Dans ce TP, vous allez construire un système de RAG (Retrieval Augmented Génération) et le publier en ligne.

Vous avez le choix complet

- du jeux de données
- des librairies : keras, ollama, huggingface, ...
- la plateforme de création de site web: streamlit par exem

Contraintes :

- vous n'utilisez que des modèles open source aussi bien pour la vectorisation, le reranking que pour la génération de la réponse
- le code doit être produit à partir d'une plateforme de coding de type windsurf, cursor etc

- vous utilisez une base de données vectorielle de type weaviate

Votre but est de développer votre intuition quant à l'efficacité et la qualité du système en fonction des différentes options en terme de modèles, de stratégie de découpage des textes, de la base de donnée

Les étapes:

## Préparation de la base référentielle

1. trouvez un jeux de données avec du contenu textes
2. si besoin chunkez / découpez le texte en extraits
3. [option] créez les vecteurs denses de chaque extrait ()

## enregistrement dans la base de données

1. choisissez une base de données vectorielle. weaviate, faiss, ...
2. insérez les données
   1. soit les vecteurs existent déjà
   2. soit les vecteurs sont générés au moment de l'enregistrement
3. testez quelque requêtes simples
   1. recherche vectorielle ou hybride
   2. algorithme de récupération : ANN ou ENN

## Retrieval

Si vous utilisez weaviate, la première étape n'est pas nécessaire.

1. [option] si besoin vectoriser la requête avec le même modèle utilisé pour les vecteurs denses du corpus de référence
2. faite la recherche et obtenez une liste de résultats d'extraits similaires
3. testez différentes métriques de similarités: cosine, euclidean, manhattan
4. valider qualitativement les résultats

## prompting

1. le prompt de base doit spécifier si le modèle n'utilise que l'info qui lui est fournie ou s'il peut utiliser ses connaissances propres
2. enrichissez le prompt avec les extraits
3. évaluer qualitativement la réponse
4. testez plusieurs modèles de génération de réponse

## Pistes d'amélioration

###  enrichir les extraits initiaux

Une fois obtenu les extraits, vous pouvez les enrichir avec des meta informations complémentaires

- extraction des entités
- résumé
- analyse des arguments ou des thèmes
- classification : sentiment, toxicité, ...
- compléter avec le nom de l'auteur, la date, le nom du document etc

### Reranker

Une fois obtenue la première liste d'extrait, vous pouvez ajouter une étape de reranking

1. choisissez un modèle de reranking
2. pour chaque extrait de la liste de résultats, associez un score entre l'extrait et la requête initiale
3. ne garder que les extraits dont le score est assez bon
4. expérimentez avec des seuils de score de filtrage différents

## Génération du code

Utilisez principalement une plateforme de coding pour générer le code

Par exemple windsurf en mode gratuit.

1. créez une repo git sur votre local
2. écrivez un readme d'instructions détaillées
3. prenez en main la plateforme windsurf
4. a chaque modification de code prenez l'habitude de commenter votre code avant de laisser l'agent le modifier
5. toujours relire

## Application en ligne (local)

Créez une page web qui permette

- de saisir une requête
- d'examiner les extraits qui sont retournés
- de voir la réponse générée

Vous ajouterez la possibilité de sélectionner certain paramètres

- modèles de génération
- étape de reranking
- température du modèle


## Publication online (web)

Streamlit donne la possibilité de publier votre repo github si elle est publique.

1. créez une repo github publique
2. publiez

