
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
semble peu naturelle. Par exemple,  