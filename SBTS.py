import random
import numpy as np

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

def search_on_neighboor_insertion(distance_matrix, individual, moves, fitness):
    tabu_list = []
    moves_counter = 0
    current = individual.copy()
    best_individual = current.copy()
    best_fitness = fitness(distance_matrix, current)

    while moves_counter < moves:
        i, j = random.sample(range(len(current)), 2)
        move = (i, j)

        if move not in tabu_list:
            node = current.pop(i)
            current.insert(j, node)

            current_fitness = fitness(distance_matrix, current)

            if current_fitness < best_fitness:
                best_individual = current.copy()
                best_fitness = current_fitness
            else:
                current.pop(j)
                current.insert(i, node)

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
                best_individual_found, best_fitness_found = search_on_neighboor_insertion(distance_matrix, individual, moves=explotation_moves, fitness=fitness)

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


