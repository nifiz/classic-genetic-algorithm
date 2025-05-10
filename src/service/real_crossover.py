import numpy as np
import random

class RealCrossover:
    def __init__(self, parent1, parent2):
        self.p1 = np.array(parent1)
        self.p2 = np.array(parent2)

    def arithmetic(self):
        child1 = (self.p1 + self.p2) / 2
        child2 = (self.p1 + self.p2) / 2
        return child1, child2

    def alpha(self, alpha=0.5):
        child1 = self.p1 + alpha * (self.p2 - self.p1)
        child2 = self.p2 + alpha * (self.p1 - self.p2)
        return child1, child2

    def linear(self):
        c1 = 0.5 * (self.p1 + self.p2)
        c2 = 1.5 * self.p1 - 0.5 * self.p2
        c3 = -0.5 * self.p1 + 1.5 * self.p2
        return random.sample([c1, c2, c3], 2)


    def alpha_beta(self, alpha=None, beta=None):
            if alpha is None:
                alpha = np.random.uniform(0, 1)
            if beta is None:
                beta = np.random.uniform(0, 1)
            child1 = alpha * self.p1 + (1 - alpha) * self.p2
            child2 = beta * self.p2 + (1 - beta) * self.p1
            return child1, child2
