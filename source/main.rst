
Les Algorithmes génétiques
##########################

Principe général 
======================

Développés depuis les années 60 par le scientifique américain John Holland, les algorithmes 
génétiques sont un type d'algorithmes s'inspirant de la théorie de l'évolution de Charles 
Darwin pour trouver la solution à un problème d'optimisation. Pour cela, on crée un ensemble 
de solutions dont les meilleures seront sélectionnées pour engendrées de nouvelles solutions 
suposément meilleures.  

Le fonctionnement d'un tel algorithme repose sur quatres grandes étapes :
    - La génération de la population
    - L'évaluation de la population
    - La sélection des individus
    - Les croisements et mutations 

.. admonition:: Vocabulaire

    Durant ce travail, nous utiliseront un vocabulaire spécifique aux algorithmes génétiques.
    L'ensemble de solutions avec lesquelles nous travaillerons est appelé **population**, chaque 
    solution particulière est appelée **induvidu**, une caractéristique d'un individu est appelée 
    **gène** et l'ensemble de ces gènes est appelé **génome**.

Génération de la population
===========================

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

Une fois la représendation des individus choisie, il faut ensuite générer la population 
qui va évoluer. Pour cela, la méthode la plus utilisée consiste à générer de manière 
aléatoire un certain nombre d'individus. Il n'existe pas de méthode générale pour déterminer 
le nombre d'individu optimal pour un problème donné mais de manière générale un grand nombre 
d'individus est un avantage car cela crée une plus grande diversité et réduit les probabilités 
de converger vers un maximum local. Cependant, il faut prendre en compte les limitation techniques
et utiliser des valeurs réalistes. 

Évaluation
==========

L'évaluation de la population consiste à déterminer quels individus sont les mieux adaptés au 
problème posé. On utilise une fonction nommée *fitness function* pour cela. Cette fonction 
revêt un rôle essentiel pour un algorithme génétique car c'est généralement elle qui prend le 
plus de temps à être évaluée et qui détermine le temps d'exécution de l'algorithme.

