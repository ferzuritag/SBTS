import matplotlib.pyplot as plt

from SBTS import SBTS
from utils.get_distance_matrix import get_distance_matrix
from instances.pr264 import points, optimal
from utils.plot_points_and_routes import plot_points_and_routes

distance_matrix = get_distance_matrix(points)
n = len(distance_matrix) - 1
exploration_moves = 25
explotation_moves = 25
exploration_factor = .1
generations = 10000
population_size = 20

print("exploration_moves = ", exploration_moves)
print("explotation_moves = ", explotation_moves)
print("exploration_factor = ", exploration_factor)
print("generations =", generations)
print("population_size", population_size)

fit, result, gen_best_history = SBTS(distance_matrix, exploration_factor=exploration_factor, generations=generations, population_size=population_size, explotation_moves = explotation_moves, exploration_moves=exploration_moves)



plot_points_and_routes(points=points, secuence=result)


print("best_fitness", fit, result)

generaciones = list(range(1, len(gen_best_history) + 1))

plt.plot(generaciones, gen_best_history, marker='.', linestyle='--', color='blue', label='Aptitud')

plt.xlabel('Generación')
plt.ylabel('Valor de Aptitud')
plt.title('Evolución del Valor de Aptitud')
plt.grid(True)
plt.axhline(y=optimal, color='red', linestyle='--', label=f'Valor óptimo: {optimal}')
plt.legend()

plt.show()