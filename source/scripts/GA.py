import random
import time
from typing import List

class GeneticAlgorithm():
    
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
    gen_size = 20
    weight_limit = 3000
    best_genome = ""

    #parametres to be modified
    parametres = {
        "crossover_rate" : 0.7,
        "two_point_crossover" : False,
        "mutation_rate" : 0.1,
        "pop_size" : 50,
        "end_condition" : 100 #number of repeted best solutions
    }

    

    def __init__(self) -> str:
        pop: list[str] = self.generate_pop(GeneticAlgorithm.parametres["pop_size"])
        pop.sort(key= self.fitness, reverse=True)
        generation = 0
        best_fitness = self.fitness(pop[0])
        counter = 0

        while counter < GeneticAlgorithm.parametres["end_condition"]:
            #print(f"generation : {generation}, best_gen : {pop[0]}, fitness : {self.fitness(pop[0])}")
            new_pop = [pop[0]]
            for i in range(GeneticAlgorithm.parametres["pop_size"]//4):
                new_pop += self.crossover(pop[2*i], pop[2*i+1])
            new_pop += self.generate_pop(GeneticAlgorithm.parametres["pop_size"] - len(new_pop))
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

        #print(f"generation : {generation}, best_gen : {pop[0]}, fitness : {self.fitness(pop[0])}")
        GeneticAlgorithm.best_genome = pop[0]
        
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
        if random.random() < cls.parametres["crossover_rate"]:
            #2 pts crossover
            if cls.parametres["two_point_crossover"]:
                index1, index2 = sorted(list(random.sample(range(len(gen1)), 2)))
                off_gen1 = gen1[:index1] + gen2[index1:index2] + gen1[index2:]
                off_gen2 = gen2[:index1] + gen1[index1:index2] + gen2[index2:]
                return off_gen1, off_gen2
            else: # 1 pt crossover
                index = random.randrange(len(gen1))
                off_gen1 = gen1[:index] + gen2[index:]
                off_gen2 = gen2[:index] + gen1[index:]
                return off_gen1, off_gen2
        else:
            return gen1, gen2

    @classmethod
    def mutation(cls, gen: str)-> str:
        if random.random() < cls.parametres["mutation_rate"]:
            index = random.randrange(len(gen))
            gen_list = list(gen)
            gen_list[index] = ('0' if gen_list[index] == 1 else '1')
            gen = ''.join(gen_list)
            return gen
        else:
            return gen


    # methods for exponential search

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
        GeneticAlgorithm.gen_size = cls.n
        GeneticAlgorithm.objects = GeneticAlgorithm.generate_objects(cls.n)
        GeneticAlgorithm.weight_limit = 0.8 * sum([item[1] for item in GeneticAlgorithm.objects])

    @staticmethod
    def time_ga() -> str:
        start = time.time()
        genetic_algorithm = GeneticAlgorithm()
        end = time.time()
        return end-start, genetic_algorithm.best_genome

    @classmethod
    def time_exp(cls) -> str:
        start = time.time()
        best = GeneticAlgorithm.find_solution(cls.n)[0]
        end = time.time()
        return end-start, best

    @classmethod
    def calculate_quality(cls, sol1, sol2) -> float:
        diff: int = 0
        for i in range(cls.n):
            if sol1[i] == sol2[i]:
                diff += 1
        return diff / cls.n

    '''
    @classmethod
    def compare_methods(cls, n: int) -> None:

        cls.reset(n)

        exp_time, exp_best = cls.time_exp()
        ga_time, ga_best = cls.time_ga()
        quality = cls.calculate_quality(exp_best, ga_best)


        print(f"Exp : best : {exp_best} \n      time : {exp_time}")
        print(f"GA  : best : {ga_best}  \n      time : {ga_time}")
        print(f"Quality : {quality *100}%")
    '''

    #prints csv of exp search times from 1 to n 
    @classmethod 
    def exp_times(cls, n: int) -> None:
        for i in range(n):
            cls.reset(i+1)
            timing, best = cls.time_exp()
            print(f"{i+1};{timing}")

    @classmethod
    def ga_average(cls, n : int, sample_size : int) -> tuple[float, float]:
        
        cls.reset(n)
        exp_time, exp_best = cls.time_exp()

        quality_avg : float = 0.0
        time_avg: float = 0.0
        for _ in range(sample_size):
            ga_time, ga_best = cls.time_ga()
            quality_avg += cls.calculate_quality(exp_best, ga_best)
            time_avg += ga_time

        quality_avg /= sample_size
        time_avg /= sample_size

        return quality_avg, time_avg, exp_time

    @classmethod
    def ga_avg_csv(cls, n_max: int, sample_size: int) -> None:
        for i in range(n_max):
            q_avg, t_avg, e_time =cls.ga_average(i+1, sample_size)
            print(f"{i+1};{t_avg};{e_time};{q_avg * 100}")

    @staticmethod
    def set_parametres(c_rate: float, m_rate: float, pop_size: int, end_condition: int, two_pts: bool) -> None:
        GeneticAlgorithm.parametres["crossover_rate"] = c_rate
        GeneticAlgorithm.parametres["two_point_crossover"] = two_pts
        GeneticAlgorithm.parametres["mutation_rate"] = m_rate
        GeneticAlgorithm.parametres["pop_size"] = pop_size
        GeneticAlgorithm.parametres["end_condition"] = end_condition
        

    @classmethod
    def test_parametres(cls, n: int, sample_size: int, param1_name: str, param1_values: List[float], param2_name: str, param2_values: List[float]) -> None:

        print(GeneticAlgorithm.parametres)
        print(param1_name, param1_values)
        print(param2_name, param2_values)
        
        param1 = param1_values[0] # param1_min
        while param1 <= param1_values[1]: # param1_max
            GeneticAlgorithm.parametres[param1_name] = param1
            param2 = param2_values[0] # param2_min
            print(param1, end='')
            while param2 <= param2_values[1]: # param2_max
                GeneticAlgorithm.parametres[param2_name] = param2
                q_avg, t_avg, e_time = cls.ga_average(n, sample_size)
                print(f";{t_avg};{q_avg * 100}", end='')
                param2 += param2_values[2] #param2_incr
            param1 += param1_values[2] #param1_incr
            print()


Time_test.set_parametres(c_rate=0.8, m_rate=0.2, pop_size=50, end_condition=100, two_pts=False)
Time_test.test_parametres(n=15, sample_size=100, param1_name="mutation_rate", param1_values=[0.0, 1, 0.1], param2_name="two_point_crossover", param2_values=[0, 0, 1])
Time_test.set_parametres(c_rate=0.8, m_rate=0.2, pop_size=50, end_condition=100, two_pts=True)
Time_test.test_parametres(n=15, sample_size=100, param1_name="mutation_rate", param1_values=[0.0, 1, 0.1], param2_name="two_point_crossover", param2_values=[0, 0, 1])

Time_test.set_parametres(c_rate=0.8, m_rate=0.2, pop_size=50, end_condition=100, two_pts=False)
Time_test.test_parametres(n=15, sample_size=100, param1_name="end_condition", param1_values=[1, 11, 1], param2_name="pop_size", param2_values=[110, 210, 10])
Time_test.test_parametres(n=15, sample_size=100, param1_name="end_condition", param1_values=[10, 110, 10], param2_name="pop_size", param2_values=[10, 110, 10])
Time_test.set_parametres(c_rate=0.8, m_rate=0.2, pop_size=50, end_condition=100, two_pts=True)
Time_test.test_parametres(n=15, sample_size=100, param1_name="end_condition", param1_values=[1, 11, 1], param2_name="pop_size", param2_values=[110, 210, 10])
Time_test.test_parametres(n=15, sample_size=100, param1_name="end_condition", param1_values=[10, 110, 10], param2_name="pop_size", param2_values=[10, 110, 10])