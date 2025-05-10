import numpy as np

class RealChromosome:
    def __init__(self, dimension, lower_bound, upper_bound, random_init=True):
        self._dimension = dimension
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        if random_init:
            self._value = np.random.uniform(low=lower_bound, high=upper_bound, size=dimension)
        else:
            self._value = np.zeros(dimension)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = np.clip(value, self._lower_bound, self._upper_bound)
