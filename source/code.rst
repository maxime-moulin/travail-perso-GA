Algorithme
##########

Voici le code qui sera utilisé pour la suite de ce travail. 

.. literalinclude:: scripts/GA.py
    :lines: 1-29

La classe *GeneticAlgortihm* comporte toutes les variables et méthodes relatives 
au fonctionnement de l'algorithme génétique en lui-même ainsi qu'à la recherche 
exhaustive qui est utilisée pour trouver la solution optimale. Les premières 
variables concernent le problème du sac à dos utilisé comme exemple, alors que 
le dictionnaire contient les différents paramètres qui peuvent être modifiés. 

.. literalinclude:: scripts/GA.py
    :lines: 33-58

La boucle de l'algorithme se trouve dans la fonction d'initialisation de la classe 
et appelle toutes les méthodes relatives à chaque étape de l'algorithme. A chaque 
génération, seule la moitié de la population est utilisée pour participer aux 
croisements et la seconde moitié est générée aléatoirement.

.. literalinclude:: scripts/GA.py
    :lines: 60-101

Ensuite se trouvent ces différentes méthodes, qui s'occupent dans l'ordre : de la 
génération aléatoire de chaque génome, de la génération d'une population aléatoire, 
de calculer la valeur d'évaluation, d'effectuer les croisements pour un ou deux points
et d'effectuer les mutations. 

.. literalinclude:: scripts/GA.py
    :lines: 106-124

Puis, nous avons les méthodes qui s'occupent de la recherche exhaustive, en créant tous 
les génomes possibles, avant de calculer leurs *fitness scores* et de trouver le maximum. 
Mais d'abord, se trouve une méthode s'occupant de générer une liste d'objets aléatoires.

.. literalinclude:: scripts/GA.py
    :lines: 127-146

Cette deuxième classe, s'occupe de faire tous les tests nécessaires sur l'algorithme. Elle 
commence par définir les paramètres de l'expérience à travers deux méthodes. 

.. literalinclude:: scripts/GA.py
    :lines: 148-168

Les méthodes suivantes servent à chronométrer les deux algorithmes de résolutions et à calculer 
la qualité de la solution obtenue. 

.. literalinclude:: scripts/GA.py
    :lines: 171-216
    :emphasize-lines: 28

Les méthodes restantes servent à calculer les moyennes pour un certain nombre de mesures et à les 
afficher par la suite. La plupart des exéprences se font à partir de la méthode *test_parametres*, 
qui prend en parmètre les paramètres qui doivent être modifiés et leur *range*, c'est à dire les 
valeurs mimimales et maximales qu'ils doivent prendre ainsi que l'incrément.  
