import random
import numpy as np

def calculate_distance(path, adj_matrix):
    dst = sum(adj_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    dst += adj_matrix[path[-1]][path[0]]
    return dst

def get_random_dna(n):
    route = list(range(n))
    random.shuffle(route)
    return route

def initialize_pop(size, n):
    return [get_random_dna(n) for _ in range(size)]

def get_fitness(population, adj_matrix):
    return [(route, 1 / calculate_distance(route, adj_matrix)) for route in population]

def select_best(population, scores, k=3):
    selected = random.sample(list(zip(population, scores)), k)
    return max(selected, key=lambda x: x[1])[0]

def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))

    child = [-1] * size
    child[start:end] = parent1[start:end]

    remaining = [gene for gene in parent2 if gene not in child]
    j = 0

    for i in range(size):
        if child[i] == -1:
            child[i] = remaining[j]
            j += 1

    return child

def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

def geneticTSP(matrix, pop_size=100, generations=500, mutation_rate=0.1):
    n = len(matrix)
    population = initialize_pop(pop_size, n)

    for generation in range(generations):

        evaluated = get_fitness(population, matrix)
        evaluated.sort(key=lambda x: x[1], reverse=True)

        selected = [select_best([p[0] for p in evaluated], [p[1] for p in evaluated]) for _ in range(pop_size // 2)]

        offspring = []

        for i in range(0, len(selected) - 1, 2):

            child1 = order_crossover(selected[i], selected[i + 1])
            child2 = order_crossover(selected[i + 1], selected[i])

            offspring.extend([child1, child2])

        population = [mutate(route, mutation_rate) for route in offspring]

    best_route, best_score = max(get_fitness(population, matrix), key=lambda x: x[1])

    return best_route, 1 / best_score

