import random

def fitness(distance_matrix, route):
    cost = 0

    for index in range(0, len(route) - 1):
        cost += distance_matrix[route[index]][route[index + 1]]

    cost += distance_matrix[0][route[0]]

    cost += distance_matrix[route[len(route) -1 ]][0]

    return cost

def generate_greedy_solution(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    sequence = []
    
    current = 0  # start from point 0 (you can change this)
    sequence.append(current)
    visited[current] = True
    
    for _ in range(n - 1):
        min_dist = float('inf')
        next_point = None
        
        for i in range(n):
            if not visited[i] and dist_matrix[current][i] < min_dist:
                min_dist = dist_matrix[current][i]
                next_point = i
        
        visited[next_point] = True
        sequence.append(next_point)
        current = next_point
    


    return sequence

def generate_random_solutions(n, m):

    solutions = []
    base = list(range(1, m+1))

    for _ in range(n):
        sol = base[:]
        random.shuffle(sol)
        solutions.append(sol)

    return solutions

def generate_random_greedy_solutions(distance_matrix, n, shuffle_moves):
    original_greedy = generate_greedy_solution(distance_matrix)
    solutions = [original_greedy]

    for _ in range(n):
        samp = shuffle(original_greedy, shuffle_moves)
        solutions.append(samp)

    return solutions

def shuffle(individual, moves):
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

def search_on_neighboor(distance_matrix, individual, moves, fitness):
    tabu_list = []
    moves_counter = 0
    current = individual.copy()
    best_individual = current.copy()
    best_fitness = fitness(distance_matrix, current)

    while moves_counter < moves:
        i, j = random.sample(range(len(current)), 2)
        move = (min(i, j), max(i, j))

        if move not in tabu_list:
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

def SBTS(distance_matrix, population_size, generations, exploration_factor, explotation_moves, exploration_moves):
    population = generate_random_solutions(population_size, len(distance_matrix) - 1)

    best_fitnesss = float('inf')
    best_individual_found = None

    gen_history = []

    # evaluation
    for individual in population:
        individual_fitness = fitness(distance_matrix, individual)
        
        if (individual_fitness < best_fitnesss):
            best_fitnesss = individual_fitness
            best_individual_found = individual


    for gen in range(generations):

        for idx, individual in enumerate(population):
            
            fitness_before_changes = fitness(distance_matrix, individual)

            if (random.random() > exploration_factor):
                # explotation behavior
                best_individual_found, best_fitness_found = search_on_neighboor(distance_matrix, individual, moves=explotation_moves, fitness=fitness)

                if best_fitness_found < fitness_before_changes:
                    population[idx] = best_individual_found
                elif (random.random() < exploration_factor):
                    population[idx] = best_individual_found

                if (best_fitness_found < best_fitnesss):
                    best_fitnesss = best_fitness_found
                    best_individual_found = best_individual_found
            else:
                new_individual = shuffle(individual, moves=exploration_moves)
                new_individual_fitness = fitness(distance_matrix, new_individual)

                if (new_individual_fitness < best_fitnesss):
                    best_fitnesss = new_individual_fitness
                    best_individual_found = new_individual

                if new_individual_fitness < fitness_before_changes:
                    population[idx] = new_individual
                
        gen_history.append(best_fitnesss)

    return best_fitnesss, best_individual_found, gen_history


