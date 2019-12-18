Projet HATVP
============

Liste des participants au projet:

   *Raissa Tatsa'a Fouodji
   *Mohammad Backer Ibrahim
   *Jahd Jabre
   *Thibault Lefebvre
   *Amaury Mouquet

Projet disponible sur **GitHub** : https://github.com/jahd/django/

**Champs d'étude du jeu de données**

La Haute Autorité pour la Transparence de la Vie Publique est une institution chargée de controler la
déontologie des responsables publics et de gérer les répertoires des représentants d'intérets. 
Elle met à disposition de tous les citoyens des fichiers open-data contenant des informations sur les 
mouvements financiers déclarés entre responsables d'interets responsables politiques. Ces fichiers sont 
librement téléchargeables sur [le site internet de la HATVP](https://www.hatvp.fr/le-repertoire/#open-data-repertoire). 

Dans le cadre de ce projet, nous avons étudié et développé une application permettant de l'exploiter les
données issues d'un lot de 16 fichiers au format .XLSX (15 tables accompagnées d'un fichier de documentation).

Méthodologie de traitement des données
======================================

La collecte des données
-----------------------

Le lot de 16 fichiers à analyser recence sous forme de tables les informations nécessaires à la compréhension 
des relations entre les représentants d'intérêts et les responsables publiques lorsque sont prises des décisions
publiques. Cela permet par exemple de connaitre les organisations ayant exercées des actions de lobying auprès
de responsables politiques, avec les noms des responsables, les dates, les montants etc.

Pour rendre l'analyse et le traitement des fichiers XSLX plus aisés, nous les avons transformé au format CSV.
En plus du fichier de documentation, nous avons donc travaillé sur les 15 tables suivantes:

1._informations_generales.csv
2._dirigeants.csv
3._collaborateurs.csv
4._clients.csv
5._affiliations.csv
6._niveaux_interventions.csv
7._domaines_interventions.csv
8._objets_activites.csv
9._secteurs_activites.csv
10._actions_menees.csv
11._beneficiaires.csv
12._decisions_concernees.csv
13._ministeres_aai_api.csv
14._observations.csv
15._exercices.csv

L'angle d'attaque de l'application 
-------------------------

- Nous souhaitons créer une application permettant à son utilisateur de rechercher les actions de lobbying effectuées entre une entreprise et les différents ministères. Grâce a cette application, inscrire le nom de l'entreprise permettra d'obtenir toutes les actions de manière claire : lorsqu'une entreprise "donne" à un ministère et lorsqu'un ministère oeuvre en faveur de l'entreprise via une action quelconque.


Exploration des données
-----------------------
- Nous avons analysé chaque table une par une afin de mieux comprendre les enjeux de ce jeu de données et d'établire un angle d'attaque. Suite à cette exploration nous avons décidé de nous focaliser sur l'intéraction entre les entreprises et les ministères afin de mieux comprendre les influences dans les hautes sphères de l'état.

Choix des tables à analyser
---------------------------
- Pour retranscrire les intéractions entre les entreprises et les ministères nous avons choisit de nous focaliser sur 3 tables:
  * Actionmenee
  * Ministeres
  * Beneficiaires
Ces 3 tables vont nous permettre de rechercher les informations que l'on souhaite avoir grace aux ID communs et via une requête SQL.
  
Construction des modèles
------------------------
- Nous avons construit 3 modèles en rapport avec les tables choisit et leur caractéristiques.

La représentation des résultats
-------------------------------
L'utilisateur de l'application devra écrire l'entreprise souhaité dans un input prévu à cet effet. L'input va déclencher une requête SQL qui va nous permettre d'afficher les résultat sur la page d'application.

Technologies utilisées pour la création de l'application
-------------------------------------------------------
L'application permettant l'interprétation des données a été dévellopée avec Python 3.8 et Django 3.0
Sqlite va nous permettre d'utiliser SQL
SQL pour faire des requêtes.
Pour le front : html/css

Difficultés rencontrées
-----------------------
Les modèles semblent être correctes mais l'importation des données pose problème et nous ne sommes pas parvenu à résoudre cette étape.
Nous avons également eu un problème au niveau du temps puisque notre groupe n'a pas pu se déplacer en cours le 1er jour du projet et nous avons eu des informations manquantes (on nous a seulement indiqué les "vues fusionnées", c'est par la suite qu'on a eu les "vues séparées")
On a essayé de pallier aux autres difficultées mineurs via des tutoriels django/sqlite.


