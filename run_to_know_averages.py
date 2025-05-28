import time
from SBTS import SBTS
from utils.get_distance_matrix import get_distance_matrix
from instances.eil51 import points

samples = 10
exploration_factor= .2
generations= 1000
population_size= 20


fit_acum = []
time_acum = []
result_acum = []

distance_matrix = get_distance_matrix(points)

exploration_moves = round(len(distance_matrix)/4)
explotation_moves = round(len(distance_matrix)/4)


print("exploration_moves = ", exploration_moves)
print("explotation_moves = ", explotation_moves)
print("exploration_factor = ", exploration_factor)
print("generations =", generations)
print("population_size", population_size)

for _ in range(samples):
    start = time.time() 
    fit, result, _ = SBTS(distance_matrix, exploration_factor=exploration_factor, generations=generations, population_size=population_size, explotation_moves = explotation_moves, exploration_moves = exploration_moves)
    
    end = time.time()
    result_acum.append(result)
    time_acum.append(end - start)
    fit_acum.append(fit)

print('Fitness')
print("max", max(fit_acum))
print("min", min(fit_acum))
print("avg", sum(fit_acum) / samples)
print('Time')
print("max", max(time_acum))
print("min", min(time_acum))
print("avg", sum(time_acum) / samples)

for l in result_acum:
    print(l)
for t in time_acum:
    print(t)

    