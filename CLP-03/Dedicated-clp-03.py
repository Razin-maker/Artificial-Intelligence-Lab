import random

T = int(input("Enter target sum T: "))
k = int(input("Enter list length k: "))

pop = [[random.randint(0,9) for _ in range(k)] for _ in range(10)]

while True:
    
    pop.sort(key=lambda x: abs(sum(x) - T))
    best = pop[0]
    if sum(best) == T:
        print("Solution found:", *best)
        break

    new_pop = pop[:2]
    while len(new_pop) < len(pop):
        p1, p2 = random.sample(pop[:5], 2)
        point = random.randrange(1, k)
        child = p1[:point] + p2[point:]
        if random.random() < 0.2:
            child[random.randrange(k)] = random.randint(0,9)
        new_pop.append(child)
    pop = new_pop