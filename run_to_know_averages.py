from utils.get_distance_matrix import get_distance_matrix
from utils.get_tsp_instance_data import get_tsp_instance_data
from benchmark import benchmark

samples = 32

_, points = get_tsp_instance_data("berlin52")
distance_matrix = get_distance_matrix(points)

n = len(distance_matrix) - 1

exploration_factor= .1
generations= 1000
population_size= 20
exploration_moves = 25
explotation_moves = 50

res, gen_best_history = benchmark(distance_matrix, samples, exploration_factor, generations, population_size, exploration_moves, explotation_moves)

print(res)

    