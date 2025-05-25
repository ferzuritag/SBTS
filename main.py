import time
from SBTS import SBTS

samples = 32
fit_acum = []
time_acum = []
result_acum = []

for _ in range(samples):
    start = time.time() 
    fit, result = SBTS(exploration_factor=.3, generations=5000, population_size=20, explotation_moves = 5, exploration_moves = 10)
    
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