import matplotlib.pyplot as plt

from SBTS import SBTS
from utils.get_distance_matrix import get_distance_matrix
from instances.eil51 import points, optimal

distance_matrix = get_distance_matrix(points)

exploration_moves = round(len(distance_matrix) /4)
explotation_moves = round(len(distance_matrix)/4)
exploration_factor =.2
generations = 1000
population_size = 20


print("exploration_moves = ", exploration_moves)
print("explotation_moves = ", explotation_moves)
print("exploration_factor = ", exploration_factor)
print("generations =", generations)
print("population_size", population_size)


fit, result, gen_best_history = SBTS(distance_matrix, exploration_factor=exploration_factor, generations=generations, population_size=20, explotation_moves = explotation_moves, exploration_moves=exploration_moves)

print("best_fitness", fit)

generaciones = list(range(1, len(gen_best_history) + 1))

plt.plot(generaciones, gen_best_history, marker='.', linestyle='--', color='blue', label='Aptitud')

plt.xlabel('Generación')
plt.ylabel('Valor de Aptitud')
plt.title('Evolución del Valor de Aptitud')
plt.grid(True)
plt.axhline(y=optimal, color='red', linestyle='--', label=f'Valor óptimo: {optimal}')
plt.legend()

plt.show()