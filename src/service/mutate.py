from ..model.chromosome import Chromosome
import random

class Mutate:
    def __init__(self, mutation_rate=0.05):
        self._mutation_rate = mutation_rate

    def one_point(self, chromosome_value: list):
        if random.random() < self._mutation_rate:
            idx = random.randint(0, len(chromosome_value) - 1)
            chromosome_value[idx] = 1 - chromosome_value[idx]
        return chromosome_value
    
    def two_point(self, chromosome_value: list):
        if random.random() < self._mutation_rate:
            idx1, idx2 = random.sample(range(len(chromosome_value)), 2)
            chromosome_value[idx1] = 1 - chromosome_value[idx1]
            chromosome_value[idx2] = 1 - chromosome_value[idx2]
        return chromosome_value

    def boundary(self, chromosome_value: list):
        if random.random() < self._mutation_rate:
            chromosome_value[0] = 1 - chromosome_value[0]
        if random.random() < self._mutation_rate:
            chromosome_value[-1] = 1 - chromosome_value[-1]
        return chromosome_value