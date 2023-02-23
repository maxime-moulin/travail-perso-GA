def fitness_function(genome):
    if sum(object.weight for object in genome) < weight_limit:
        return sum(object.value for object in genome)
    else :
        return 0