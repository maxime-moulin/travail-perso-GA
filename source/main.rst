
Les Algorithmes génétiques
##########################

Principe général 
======================

Développés depuis les années 60 par le scientifique américain John Holland, les algorithmes 
génétiques sont un type d'algorithmes s'inspirant de la théorie de l'évolution de Charles 
Darwin pour trouver la solution à un problème d'optimisation. Pour cela, on crée un ensemble 
de potentielles solutions dont les meilleures seront sélectionnées pour engendrées de 
nouvelles solutions suposément meilleures.  

Le fonctionnement d'un tel algorithme repose sur trois grandes étapes :
    * La génération de la population
    * L'évaluation et la sélection des individus
    * Les croisements et mutations 

.. admonition:: Vocabulaire

    Durant ce travail, nous utiliserons un vocabulaire spécifique aux algorithmes génétiques.
    L'ensemble de solutions potentielles avec lesquelles nous travaillerons est appelé 
    **population**, chaque solution potentielle est appelée **induvidu**, une caractéristique 
    d'un individu est appelée **gène** et l'ensemble de ces gènes est appelé **génome**.

Génération de la population 
===========================

Représentation du génome
------------------------

Pour pouvoir mettre en application un algorithme génétique, il faut tout d'abord pouvoir
modéliser les individus et leur génombre de manière efficace. Il existe plusieurs 
façons de faire cela mais la plus simple est la représentation binaire. Cela consiste à 
représenter le génome par une chaîne binaire composée de "0" et de "1. Dans le cas du 
problème du sac à dos, chaque objet pouvant être mis dans le sac est un des gènes et sa 
présence ou son absence sont indiquées par respectivement un "1" ou un "0". 

.. exemple

Le fait de coder le génome d'un individu de cette façon a l'avantage d'être simple donne 
de nombreuses possibilité d'enjambements mais pour certains problèmes cette représentation 
semble peu naturelle. Par exemple, si l'on cherche une chaîne de caractères il est plus 
évident que chaque gène soit un des caractères de la chaîne. C'est pour cela qu'on utilise 
un codage se basant sur des nombres entiers, des nombres à virgule flottante ou des caractères 
quelconques. Il existe également différentes façons de représenter le génome, par exemple sous 
forme d'arbre, ou d'optimiser son codage comme le *Gray coding* mais la façon dont les 
individus sont modélisés dépend essentiellement du problème auquel on fait face 
et sert de base pour toutes les opérations qui agiront sur leurs génomes. 

Population initiale
-------------------

Une fois la représendation des individus choisie, il faut ensuite générer la population 
qui va évoluer. Pour cela, la méthode la plus utilisée consiste à générer de manière 
aléatoire un certain nombre d'individus. Il n'existe pas de méthode générale pour déterminer 
le nombre d'individu optimal pour un problème donné mais de manière générale un grand nombre 
d'individus est un avantage car cela crée une plus grande diversité et réduit les probabilités 
de converger vers un maximum local. Cependant, il faut prendre en compte les limitation techniques
et utiliser des valeurs réalistes. 

Cette population représente la première génération d'individus. Il va ensuite s'agir de la faire 
évoluer pour donner naissances à d'autres générations mieux adaptées au problème. La première 
étape de cette évolution est l'évaluation. 

Évaluation et sélection
=======================

Évaluation
----------

L'évaluation de la population consiste à déterminer quantitativement quels individus sont 
les mieux adaptés au problème posé. On utilise une fonction nommée *fitness function* pour 
cela. Cette fonction assigne une valeur plus ou moins grande à chaque individu, récompensant 
plus les *meilleurs* et moins les *moins bons*. La façon de calculer cela dépend encore une 
fois du problème mais elle doit non seulement pouvoir déterminer les individus qui correspondent
à une solution du problème mais aussi pouvoir classer ceux qui n'y correspondent pas ; une 
telle fonction retournant "1" pour les solutions du problème et "0" pour les autres individus 
serait très mauvaise car elle rendrait impossible l'amélioration.

La *fitness function* du problème du sac à dos cherche à maximiser la valeur transportée tout
en respectant la limite de poids imposée et peut être conçue de la façon suivante :

.. literalinclude:: scripts/exemple.py
    :lines: 1-5

Cette fonction revêt également un rôle essentiel pour un algorithme génétique car c'est 
généralement elle qui prend le plus de temps à être évaluée et qui détermine donc le temps 
d'exécution de l'algorithme. Il est donc nécessaire de la rendre la plus efficace possible 
pour économiser du temps. 

Sélection
---------

Après l'évaluation des individus, il s'agit de passer à leur sélection. Comme dans la nature 
où les individus les mieux adaptés à l'environnement survivent et peuvent donner naissance à
la génération suivante, la séléction consiste à choisir parmis les différents individus lesquelles
vont transmettre leur génome à la génération suivante. Il existe plusieurs façons de déterminer 
ces parents. 

Premièrement, il y a la sélection par *roue de la fortune* qui consiste à 
sélectionner un individu de manière aléatoire mais rendant la probabilité d'être choisi 
proportionnelle à la valeur de l'évaluation. Cette méthode est efficace car elle prend en compte 
l'adaptation au problème mais elle peut être difficile à appliquer et un individu risque d'être 
sélectionné plusieurs fois. Une autre manière de sélectionner des individus est nommée 
*Stochastic universal sampling* (SUS) et permet de réduire ce risque et d'augmenter les chances 
d'être sélectionné au moins une fois des meilleurs individus.

Il y a également la sélection par rang où l'on sélection arbitrairement les k meilleurs individus. 
Cela simplifie le processus mais la sélection se fait indépendamment des valeurs d'évaluation. 
Cette méthode se révèle efficace losque les valeurs d'évaluation sont très proches, notamment 
en fin de simulation.

De plus, on peut retrouver la sélection par tournoi. On choisi un nombre arbitraire d'individus 
aléatoirement parmi la population et on sélectionne le meilleur de ce groupe. Puis, ce processus 
est répété jusqu'à avoir le bon nombre de parents. Les avantages de cette méthode sont sa 
simplicité à être mise en oeuvre et son efficacité à être implémentée sur une architecture en 
parallèle.

D'autres méthodes de sélection existent encore comme la sélection aléatoire ou la sélection 
basée sur une récompense qui ne seront pas détaillées ici. Les individus sélectionnés ne 
représentent cependant pas forcément la totalité de la génération suivante et une partie de 
celle-ci peut être générée aléatoirement comme pour la première génération ce qui permet 
d'amener de nouveaux gènes qui n'étaient pas présents auparavant.

Opérateurs génétiques
=====================

Les individus parents ayant été sélectionné, il faut créer les "enfants". Il y a certes la 
possiblilité de copier tels quels les parents mais on lui préfère souvent l'utilisation 
d'opérateurs génétiques, à savoir les croisements (*crossover*) et les mutations.  

Croisements
-----------

Mutations
---------

Élitisme
--------