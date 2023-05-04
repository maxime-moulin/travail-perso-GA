.. _conclusion.rst:

Conclusion
##########

Les algorithmes génétiques sont efficaces pour résoudre certains problèmes 
qui ne peuvent pas être résolus en temps polynomial, ce qui explique leur large utilisation
dans une multitude de milieux différents. Ils s'inspirent de la manière dont 
l'évolution fonctionne dans la nature pour chercher la solution la plus adaptée à un 
problème donné. Cependant, pour chaque étape de l'algorithme, il existe un grand nombre 
de façons de procéder différentes et déterminer laquelle convient le mieux pour un 
problème donné n'est pas tout le temps aisé. 

Pour résoudre le problème du sac à dos, il est naturel d'utiliser certaines méthodes car 
elles sont plus simple à mettre en place, comme le fait de travailler avec un codage 
binaire par exemple. Mais il reste, tout de même de nombreux paramètres à optimiser. 
Ceux sur lesquels nous nous sommes attardés sont les probablilité de croisement et de 
mutation, la condition de fin, la taille de la population et le fait que le croisement 
se fasse avec un ou deux points. 

Nous avons d'abord constaté que le taux de mutation n'a qu'un effet restreint alors 
que le taux de croisement permet, si l'on choisit une valeur élevée, de réduire 
considérablement le temps d'exécution et d'améliorer la qualité de la solution 
obtenue. Néanmoins, le fait que le croisement se fasse à un ou deux point importe 
peu. De plus, la taille de la population et la condition de fin augmentent, 
toutes les deux, le temps d'exécution de manière linéaire. La condition de fin ayant un 
effet négligeable sur la qualité pour plus de 30 générations, il est préférable de 
prendre cette valeur-ci pour optimiser la qualité et le temps. Cependant, une plus 
grande population est bénéfique pour obtenir une meilleure solution. Il faut donc 
faire un compromis entre le temps et la qualité pour obtenir le meilleur des deux et une 
valeur de 70 pourrait être un bon compromis.

Enfin, nous avons pu remarquer que l'optimisation d'un algorithme génétique est un problème 
en lui-même et qu'il est composés de nombreux paramètres, dont il est difficile de connaître 
la valeur optimale. Un moyen de trouver une solution à cela sans tester toutes les possibilité, 
comme il a été fait dans ce projet, serait donc d'utiliser un autre algorithme génétique. 