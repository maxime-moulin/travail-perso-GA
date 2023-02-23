import random
import time

class GeneticAlgorithm():

    crossover_rate = 0.7
    mutaton_rate = 0.1
    max_fitness = 1310
    objects = [[100,     70,    "cap"    ],
                [10,     38,    "socks"  ],
                [60,     350,   "mug"    ],
                [30,     192,   "bottle" ],
                [500,    2200,  "laptop" ],
                [150,    160,   "earbuds"],
                [500,    200,   "phone"  ],
                [5,      25  ,  "mints"  ],
                [40,     333 ,  "notepad"],
                [15,     80  ,  "tissues"]]
    pop_size = 50
    gen_size = 20
    weight_limit = 3000
    end_condition = 100 #number of repeted best solutions

    def __init__(self):
        pop: list[str] = self.generate_pop(GeneticAlgorithm.pop_size)
        pop.sort(key= self.fitness, reverse=True)
        generation = 0
        best_fitness = self.fitness(pop[0])
        counter = 0

        while counter < GeneticAlgorithm.end_condition:
            #print(f"generation : {generation}, best_gen : {pop[0]}, fitness : {self.fitness(pop[0])}")
            new_pop = [pop[0]]
            for i in range(GeneticAlgorithm.pop_size//4):
                new_pop += self.crossover(pop[2*i], pop[2*i+1])
            new_pop += self.generate_pop(GeneticAlgorithm.pop_size - len(new_pop))
            for gen in new_pop:
                gen = self.mutation(gen)
            pop = new_pop
            pop.sort(key= self.fitness, reverse=True)
            generation += 1

            new_fitness = self.fitness(pop[0])
            if new_fitness != best_fitness: 
                counter = 0
                best_fitness = new_fitness
            else :
                counter += 1

        print(f"generation : {generation}, best_gen : {pop[0]}, fitness : {self.fitness(pop[0])}")

        
    @classmethod
    def generate_genome(cls)-> str:
        return ''.join([random.choice(('0','1')) for _ in range(cls.gen_size)])

    @classmethod
    def generate_pop(cls, size: int)-> list[str]:
        return [cls.generate_genome() for _ in range(size)]

    @staticmethod
    def fitness(genome: str)-> int:
        if sum((int(value) * GeneticAlgorithm.objects[i][1]) for i, value in enumerate(genome)) \
            <= GeneticAlgorithm. weight_limit:
            return sum((int(value) * GeneticAlgorithm.objects[i][0]) for i, value in enumerate(genome))
        return 0 

    @classmethod
    def crossover(cls, gen1: str, gen2: str):
        if random.random() < cls.crossover_rate:
            index = random.randrange(1,len(gen1)-1)
            off_gen1 = gen1[:index] + gen2[index:]
            off_gen2 = gen2[:index] + gen1[index:]
            return off_gen1, off_gen2
        else:
            return gen1, gen2

    @classmethod
    def mutation(cls, gen: str)-> str:
        if random.random() < cls.mutaton_rate:
            index = random.randrange(len(gen))
            gen_list = list(gen)
            gen_list[index] = ('0' if gen_list[index] == 1 else '1')
            gen = ''.join(gen_list)
            return gen
        else:
            return gen

    @staticmethod
    def generate_objects(n: int) -> list[list[int]]:
        return [[random.randint(0, 500), random.randint(0, 2500)] for _ in range(n)]

    @staticmethod
    def generate_all(n: int) -> list[int]:
        all = [str(bin(item))[2:] for item in list(range(2**n))]
        return ['0'*(n - len(item)) + item for item in all]

    @classmethod
    def generate_fitness(cls, n: int) -> tuple[list[int], list[str]]:
        all = cls.generate_all(n)
        return ([cls.fitness(item) for item in all], all)

    @classmethod
    def find_solution(cls, n : int) -> tuple[str, int]:
        fitnesses, gens = cls.generate_fitness(n)
        index, best = max(enumerate(fitnesses),key=lambda x: x[1])
        return gens[index], best


class Time_test:
    n = 10
    GeneticAlgorithm.gen_size = n
    GeneticAlgorithm.objects = GeneticAlgorithm.generate_objects(n)
    GeneticAlgorithm.weight_limit = 0.8 * sum([item[1] for item in GeneticAlgorithm.objects])

    @classmethod
    def reset(cls, n: int) -> None:
        cls.n = n
        GeneticAlgorithm.gen_size = n
        GeneticAlgorithm.objects = GeneticAlgorithm.generate_objects(n)
        GeneticAlgorithm.weight_limit = 0.8 * sum([item[1] for item in GeneticAlgorithm.objects])

    @staticmethod
    def time_ga() -> None:
        start = time.time()
        genetic_algorithm = GeneticAlgorithm()
        end = time.time()
        print(f"{(end-start) * 1000} ms")

    @classmethod
    def time_exp(cls) -> None:
        start = time.time()
        print(GeneticAlgorithm.find_solution(cls.n)[0])
        end = time.time()
        print(f"{(end-start) * 1000} ms")


Time_test.time_exp()
Time_test.time_ga()