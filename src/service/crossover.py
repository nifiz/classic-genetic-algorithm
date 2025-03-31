import random
import numpy as np

class Crossover:
    def __init__(self, parent1: list, parent2: list):
        self._parent1 = parent1
        self._parent2 = parent2

    def one_point(self):
        point = random.randint(1, len(self._parent1) - 1)
        child1 = np.concatenate((self._parent1[:point], self._parent2[point:]))
        child2 = np.concatenate((self._parent2[:point], self._parent1[point:]))
        return child1, child2

    def two_point(self):
        point1 = random.randint(1, len(self._parent1) - 1)
        point2 = random.randint(1, len(self._parent1) - 1)
        if point1 > point2:
            point1, point2 = point2, point1

        child1 = np.concatenate((self._parent1[:point1], self._parent2[point1:point2], self._parent1[point2:]))
        child2 = np.concatenate((self._parent2[:point1], self._parent1[point1:point2], self._parent2[point2:]))
        return child1, child2

    def uniform(self):
        child1 = np.copy(self._parent1)
        child2 = np.copy(self._parent2)

        for i in range(len(self._parent1)):
            if random.random() < 0.5:  # probability of swapping genes - 50%
                child1[i], child2[i] = child2[i], child1[i]

        return child1, child2

    def granular(self):
        # parents should have the same length
        length = len(self._parent1)
        child1 = np.copy(self._parent1)
        child2 = np.copy(self._parent2)

        for i in range(length):
            if random.random() < 0.75:  # parent1's gene for child1 - higher probability
                child1[i] = self._parent1[i]
                child2[i] = self._parent2[i]  # parent2's gene for child2
            else: # genes swap for the rest 25%
                 child1[i], child2[i] = self._parent2[i], self._parent1[i]

        return child1, child2