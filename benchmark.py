import time
from SBTS import SBTS

def benchmark(distance_matrix,samples, exploration_factor,generations ,population_size, exploration_moves, explotation_moves):
    fit_acum = []
    time_acum = []
    result_acum = []
    best_fit = float('inf')
    best_fit_history = None

    for n_test in range(samples):
        start = time.time() 
        fit, result, gen_history = SBTS(distance_matrix, exploration_factor=exploration_factor, generations=generations, population_size=population_size, explotation_moves = explotation_moves, exploration_moves = exploration_moves)
        print(fit)
        if fit < best_fit:
            best_fit = fit
            best_fit_history = gen_history

        end = time.time()
        result_acum.append(result)
        time_acum.append(end - start)
        fit_acum.append(fit)
        print(f"Test {n_test + 1} finished")


    fitness_minimum = min(fit_acum)
    fitness_maximum = max(fit_acum)
    fitness_avg = sum(fit_acum) / samples

    time_maximum = max(time_acum)
    time_minimum = min(time_acum)
    time_avg = sum(time_acum) / samples

    return {
        'fitness_avg': fitness_avg,
        'fitness_maximum': fitness_maximum,
        'fitness_minimum': fitness_minimum,
        'time_avg': time_avg,
        'time_maximum': time_maximum,
        'time_minimum': time_minimum
    }, best_fit_history