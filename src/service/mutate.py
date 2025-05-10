from ..model.chromosome import Chromosome
import random

class Mutate:
    def __init__(self, mutation_rate=0.05, gaussian_mean=0.0, gaussian_std=1.0, uniform_range=(-1.0, 1.0)):
        self._mutation_rate = mutation_rate
        self._gaussian_mean = gaussian_mean
        self._gaussian_std = gaussian_std
        self._uniform_range = uniform_range


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
    
    def uniform(self, chromosome_value: list):
        for i in range(len(chromosome_value)):
            if random.random() < self._mutation_rate:
                chromosome_value[i] += random.uniform(*self._uniform_range)
        return chromosome_value
    
    def gaussian(self, chromosome_value: list):
        for i in range(len(chromosome_value)):
            if random.random() < self._mutation_rate:
                # Dodaj przesunięcie i zaokrąglij do 0 lub 1
                mutated = chromosome_value[i] + random.gauss(self._gaussian_mean, self._gaussian_std)
                chromosome_value[i] = int(round(min(1, max(0, mutated))))
        return chromosome_value


