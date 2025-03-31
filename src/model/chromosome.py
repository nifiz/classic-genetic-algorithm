import numpy as np

class Chromosome:
    def __init__(self, length, random=True):
        self._length = length
        self._value = []
        if random:
            self._value = np.random.randint(2, size=self._length)

    def set_value(self, value):
        self._value = value
        self._length = len(value)

    def get_value(self):
        return self._value