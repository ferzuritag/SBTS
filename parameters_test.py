from SBTS import SBTS
from utils.get_distance_matrix import get_distance_matrix
from instances.att48 import points
from benchmark import benchmark
import itertools

samples = 5

exploration_factor= .2
generations= 1000
population_size= 20
exploration_moves = 20
explotation_moves = 20

n = len(get_distance_matrix(points)) - 1


posible_for_exploration = [.1, .2,.3]
posible_for_population = [10, 20, 30]
posible_for_generations = [1000] 
posible_for_explotation_moves = [20,30]
posible_for_exploration_moves = [50, 100]

com_list = list(itertools.product(posible_for_exploration,posible_for_population,posible_for_generations,posible_for_explotation_moves, posible_for_exploration_moves))

for com in com_list:
    bench_res = benchmark(get_distance_matrix(points), samples,com[0], com[2], com[1], com[3], com[4])
    print("exp_factor=", com[0])
    print("population=", com[1])
    print("generation=", com[2])
    print("explotation_moves=", com[3])
    print("exploration_moves=", com[4])
    print("fitness_avg=", bench_res['fitness_avg'])
    print("time_avg=", bench_res['time_avg'])
    print("=========================================")


# res = benchmark(get_distance_matrix(points), samples,exploration_factor,generations, population_size, exploration_moves, explotation_moves)

# print(res)

    