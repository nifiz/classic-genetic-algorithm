import random

class Inversion:
    def __init__(self, mutation_rate):
        self._mutation_rate = mutation_rate

    def apply(self, chromosome):
        if random.random() < self._mutation_rate:
            start = random.randint(0, len(chromosome) - 2)
            end = random.randint(start + 1, len(chromosome))
            chromosome[start:end] = list(reversed(chromosome[start:end]))
        return chromosome