from utils.get_distance_matrix import get_distance_matrix
from instances.ts225 import points, optimal
from benchmark import benchmark
import matplotlib.pyplot as plt

samples = 32
distance_matrix = get_distance_matrix(points)

n = len(distance_matrix) - 1

exploration_factor= .2
generations= 1000
population_size= 20
exploration_moves = 25
explotation_moves = 25



res, gen_best_history = benchmark(distance_matrix, samples,exploration_factor,generations, population_size, exploration_moves, explotation_moves)


print("best_fitness", res['fitness_minimum'])
generaciones = list(range(1, len(gen_best_history) + 1))

plt.plot(generaciones, gen_best_history, marker='.', linestyle='--', color='blue', label='Aptitud')

plt.xlabel('Generación')
plt.ylabel('Valor de Aptitud')
plt.title('Evolución del Valor de Aptitud')
plt.grid(True)
plt.axhline(y=optimal, color='red', linestyle='--', label=f'Valor óptimo: {optimal}')
plt.legend()

plt.show()

    