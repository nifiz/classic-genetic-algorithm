import numpy as np

class Chromosome:
    def __init__(self, length, random=True, representation='binary', lower_bound=-5, upper_bound=5):
        self._length = length
        self._value = []
        self._representation = representation
        if random:
            #self._value = np.random.randint(2, size=self._length)
            if representation == 'binary':
                self._value = np.random.randint(2, size=self._length)
            elif representation == 'real':
                self._value = np.random.uniform(lower_bound, upper_bound, size=self._length)

    def set_value(self, value):
        self._value = value
        self._length = len(value)

    def get_value(self):
        return self._value