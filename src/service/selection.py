from ..model.population import Population
import random


class Selection:
    def __init__(self, population: Population, population_fitness: list, offspring_percentage: int):
        self._population_values = population.get_population_values()
        self._population_fitness = population_fitness
        self._offspring_percentage = offspring_percentage
    
    def pops_to_return(self) -> int:
        pops = int(len(self._population_values)*(self._offspring_percentage/100))
        pops += (pops < 2)*(2 - pops)
        pops &= ~1
        return pops
        
    def best(self):
        sorted_pop = sorted(zip(self._population_values, self._population_fitness), key=lambda x: x[1])
        return [x[0] for x in sorted_pop[:self.pops_to_return()]]


    # Guaranteed to return an even integer in range [2, len(self._population_values)].
    def roulette(self) -> list[list[int]]:
        total_fitness = sum(self._population_fitness)
        selection_probs = [(1 - (f/total_fitness)) for f in self._population_fitness]

        return random.choices(self._population_values, 
                              weights=selection_probs, 
                              k=self.pops_to_return())


    def tournament(self) -> list[list[int]]:
        selected = []
        tournament_size = max(2, len(self._population_values) // 10)
        
        for _ in range(self.pops_to_return()):
            candidates = random.sample(list(zip(self._population_values, self._population_fitness)), k=tournament_size)
            selected.append(min(candidates, key=lambda x: x[1])[0])
        return selected
