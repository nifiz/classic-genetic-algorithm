from ..model.chromosome import Chromosome
from ..util.bin_to_decim import binary_to_decimal
from math import sin, pow, pi

class FitnessFunction:
    def __init__(self, lower_bound=-5, upper_bound=5, precision=8, representation='binary'):
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._precision = precision
        self._representation = representation
    #def __init__(self, lower_bound=-5, upper_bound=5, precision=8):
     #   self._lower_bound = lower_bound
     #  self._upper_bound = upper_bound
     #   self._precision = precision

    def _decode(self, chromosome_value: list):
        if self._representation == 'binary':
            return binary_to_decimal(chromosome_value, self._lower_bound, self._upper_bound, self._precision)
        return chromosome_value  # zakładamy, że to lista floatów

     

    def hypersphere(self, chromosome_value: list) -> float:
        decoded_values = self._decode(chromosome_value)
        return sum(x**2 for x in decoded_values)
        #decoded_values = binary_to_decimal(chromosome_value, self._lower_bound, self._upper_bound, self._precision)
        #return sum(x**2 for x in decoded_values)
    
    def michalewicz(self, chromosome_value: list, m=10) -> float:
        decoded_values = self._decode(chromosome_value)
        return -sum(
            sin(decoded_values[i]) * pow(sin((i+1) * pow(decoded_values[i], 2) / pi), 2 * m)
            for i in range(len(decoded_values))
        )
        # The parameter m defines the steepness of they valleys and ridges.
        #decoded_values = binary_to_decimal(chromosome_value, self._lower_bound, self._upper_bound, self._precision)
        #return -sum(sin(decoded_values[i])*pow(sin((i+1)*pow(decoded_values[i],2)/pi),2*m) for i in range(len(decoded_values)))

