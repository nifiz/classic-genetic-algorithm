from .chromosome import Chromosome

class Population:
    def __init__(self, size, precision, num_of_variables=2, random=True):
        self._size = size
        self._value: list[Chromosome] = []
        self._precision = precision
        if random:
            self._value = [Chromosome(precision * num_of_variables) for _ in range(size)]
    
    def set_population(self, value):
        self._value = []
        for val in value:
            chrom = Chromosome(0,random=False)
            chrom.set_value(val)
            self._value.append(chrom)
        self._size = len(self._value)
    
    def get_population_values(self):
        return [chrom.get_value() for chrom in self._value]
    
    def get_population(self):
        return self._value

    def get_precision(self):
        return self._precision