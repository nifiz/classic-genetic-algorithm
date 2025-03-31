import random

class ElitarStrategy:
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, population_values, population_fitness):
        elite_count = max(1, int(len(population_values) * (self.percentage / 100)))
        best_individuals = sorted(zip(population_values, population_fitness), key=lambda x: x[1])[:elite_count]
        return [ind[0] for ind in best_individuals]
