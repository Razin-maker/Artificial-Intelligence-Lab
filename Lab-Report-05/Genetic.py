import random

# Calculate fitness: higher fitness = fewer conflicts
def fitness(individual):
    conflicts = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return -conflicts

# Generate a random individual (a potential solution)
def generate_individual(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Select parents using tournament selection
def select_parent(population):
    tournament = random.sample(population, 5)
    return max(tournament, key=lambda ind: ind[1])[0]

# Crossover two parents to produce an offspring
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Mutate an individual
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        individual[random.randint(0, len(individual) - 1)] = random.randint(0, len(individual) - 1)

# Solve the N-Queens problem
def genetic_algorithm(n, population_size, mutation_rate, max_generations):
    # Initialize population
    population = [(generate_individual(n), 0) for _ in range(population_size)]
    for generation in range(max_generations):
        # Evaluate fitness
        population = [(ind, fitness(ind)) for ind, _ in population]
        population.sort(key=lambda ind: ind[1], reverse=True)

        # Check for solution
        if population[0][1] == 0:
            return population[0][0], generation

        # Create the next generation
        next_generation = []
        for _ in range(population_size // 2):
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_generation.append((child1, 0))
            next_generation.append((child2, 0))

        population = next_generation

    return None, max_generations

# Input from the user
n = int(input("Enter the number of queens (N): "))
population_size = int(input("Enter the population size: "))
mutation_rate = float(input("Enter the mutation rate (e.g., 0.1 for 10%): "))
max_generations = int(input("Enter the maximum number of generations: "))

# Run the algorithm
solution, generations = genetic_algorithm(n, population_size, mutation_rate, max_generations)

# Display results
if solution:
    print(f"Solution found in {generations} generations: {solution}")
else:
    print("No solution found within the maximum number of generations.")
