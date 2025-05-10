from .chromosome import Chromosome
from .real_chromosome import RealChromosome

class Population:
    #def __init__(self, size, precision, num_of_variables=2, random=True):
    def __init__(self, size, precision_or_dim, num_of_variables=2,
                 lower_bound=-5, upper_bound=5, representation='binary', random=True):
        self._size = size
        self._representation = representation
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._precision_or_dim = precision_or_dim
        self._value = []

        if random:
            for _ in range(size):
                if representation == 'binary':
                    #self._value.append(Chromosome(precision_or_dim * num_of_variables))
                    self._value.append(
                        Chromosome(
                            precision_or_dim * num_of_variables,
                            random=random,
                            representation=self._representation,
                            lower_bound=lower_bound,
                            upper_bound=upper_bound
                        )
                    )
                elif representation == 'real':
                    self._value.append(RealChromosome(num_of_variables, lower_bound, upper_bound))
                else:
                    raise ValueError("Unsupported representation type")

    #poprzedni kod do def
        #self._size = size
        #self._value: list[Chromosome] = []
        #self._precision = precision
        #if random:
        #    self._value = [Chromosome(precision * num_of_variables) for _ in range(size)]
    
    def set_population(self, value):
        self._value = []
        for val in value:
            if self._representation == 'binary':
                #chrom = Chromosome(len(val), random=False)
                chrom = Chromosome(
                    len(val),
                    random=False,
                    representation='binary',
                    lower_bound=self._lower_bound,
                    upper_bound=self._upper_bound
                )
            else:
                chrom = RealChromosome(len(val), self._lower_bound, self._upper_bound, random_init=False)
            chrom.set_value(val)
            self._value.append(chrom)
        self._size = len(self._value)

        #poprzedni kod do set_population
            #chrom = Chromosome(0,random=False)
            #chrom.set_value(val)
            #self._value.append(chrom)
        #self._size = len(self._value)
    
    def get_population_values(self):
        return [chrom.get_value() for chrom in self._value]
    
    def get_population(self):
        return self._value

    def get_precision(self):
        #return self._precision
        return self._precision_or_dim