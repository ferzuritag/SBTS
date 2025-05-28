import random

def fitness(distance_matrix, route):
    cost = 0

    for index in range(0, len(route) - 1):
        cost += distance_matrix[route[index]][route[index + 1]]

    cost += distance_matrix[0][route[0]]

    cost += distance_matrix[route[len(route) -1 ]][0]

    return cost

def generate_random_solutions(n, m):

    solutions = []
    base = list(range(1, m+1))

    for _ in range(n):
        sol = base[:]
        random.shuffle(sol)
        solutions.append(sol)

    return solutions

def apply_random_swaps_to_all(arrays, x):

    n = len(arrays[0])
    moves = [tuple(random.sample(range(n), 2)) for _ in range(x)]

    for idx in range(len(arrays)):
        for i, j in moves:
            arrays[idx][i], arrays[idx][j] = arrays[idx][j], arrays[idx][i]

def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((neighbor, (i, j))) 
    return neighbors

def do_moves(individual, moves):
    tabu_list = []
    moves_counter = 0
    individual = individual.copy()

    while moves_counter < moves:
        i, j = random.sample(range(len(individual)), 2)
        move = (min(i, j), max(i, j))

        if move not in tabu_list:
            individual[i], individual[j] = individual[j], individual[i]
            
            tabu_list.append(move)

            moves_counter += 1

    return individual

def do_moves_over_the_same(distance_matrix, individual, moves, fitness):
    tabu_list = []
    moves_counter = 0
    current = individual.copy()
    best_individual = current.copy()
    best_fitness = fitness(distance_matrix, current)

    while moves_counter < moves:
        i, j = random.sample(range(len(current)), 2)
        move = (min(i, j), max(i, j))

        if move not in tabu_list:
            # Realizar el movimiento sobre el actual
            current[i], current[j] = current[j], current[i]
            current_fitness = fitness(distance_matrix, current)

            if current_fitness < best_fitness:
                best_individual = current.copy()
                best_fitness = current_fitness
            else:
                # Si no mejora, deshacer el movimiento
                current[i], current[j] = current[j], current[i]

            tabu_list.append(move)
            moves_counter += 1

    return best_individual, best_fitness

#426
def SBTS(distance_matrix, population_size, generations, exploration_factor, explotation_moves, exploration_moves):
    population = generate_random_solutions(population_size, len(distance_matrix) - 1)

    alpha_fitness = float('inf')
    alpha_individual = None

    gen_history = []

    # evaluation
    for individual in population:
        individual_fitness = fitness(distance_matrix, individual)
        
        if (individual_fitness < alpha_fitness):
            alpha_fitness = individual_fitness
            alpha_individual = individual



    for gen in range(generations):

        for idx, individual in enumerate(population):
            
            fitness_before_changes = fitness(distance_matrix, individual)

            if (random.random() > exploration_factor):
                # explotation behavior
                best_individual_found, best_fitness_found = do_moves_over_the_same(distance_matrix, individual, moves=explotation_moves, fitness=fitness)

                if best_fitness_found < fitness_before_changes:
                    population[idx] = best_individual_found
                elif (random.random() < exploration_factor):
                    population[idx] = best_individual_found

                if (best_fitness_found < alpha_fitness):
                    alpha_fitness = best_fitness_found
                    alpha_individual = best_individual_found
            else:
                new_individual = do_moves(individual, moves=exploration_moves)
                new_individual_fitness = fitness(distance_matrix, new_individual)

                if (new_individual_fitness < alpha_fitness):
                    alpha_fitness = new_individual_fitness
                    alpha_individual = new_individual

                if new_individual_fitness < fitness_before_changes:
                    population[idx] = new_individual

                
                    
        gen_history.append(alpha_fitness)

    return alpha_fitness, alpha_individual, gen_history


