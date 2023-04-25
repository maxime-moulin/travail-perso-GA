
Analyse
#######

L'objectif de cette section est d'optimiser l'algorithme génétique, présenté précédemment, 
servant à la résolution du problème du sac à dos. Deux éléments différents sont étudiés : 
le temps d'exécution du programme, qui doit être minimisé, ainsi que la qualité de la 
solution obtenue, c'est-à-dire à quel point celle-ci est proche de la solution optimale. 
Or, ces résultats dépendent d'une multitude de paramètres différents et il est hautement 
probable qu'ils ne soient pas indépendants les uns des autres, ce qui nous empêche de 
trouver leurs valeurs optimales en les étudiant séparément. C'est pourquoi nous allons en 
étudier qu'un nombre restreint, à savoir les probabilités de croisement, avec un ou deux 
points, et de mutation, la taille de la population et la condition de fin. Il serait, de 
plus, intéressant d'étudier la façon dont les valeurs obtenues évoluent en fonction de 
la taille du génome relatif au problème. Cependant, le temps nécessaire pour trouver la 
solution optimale à l'aide d'une recherche exhaustive évoluant exponentiellement avec la 
taille du génome, il serait alors difficile de déterminer la qualité d'une solution pour 
une telle taille. Il faudrait alors trouver une autre façon de déterminer la solution 
optimale. En se basant sur l'exemple de l'introduction, il semble donc que 15 bits soit 
une taille adéquate. 


