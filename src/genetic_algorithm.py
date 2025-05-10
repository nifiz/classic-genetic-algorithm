from .model.population import Population
from .service.fitness_function import FitnessFunction
from .service.selection import Selection
from .service.crossover import Crossover
from .service.mutate import Mutate
from .util.bin_to_decim import binary_to_decimal
from .util.plotter import Plotter3D
from .service.inversion import Inversion
from .service.elitar_strategy import ElitarStrategy
from math import ceil
import random


class GeneticAlgorithm:
    def __init__(self, population_size=500, precision=20, epochs=60, 
                    offspring_percentage=50, 
                    lower_bound=-5, upper_bound=5,
                    selection_method="roulette", crossover_method="one_point", 
                    mutation_method="one_point", fitness_function='hypersphere', 
                    mutation_rate=0.05, elitar_strategy=True, plot: Plotter3D=None,
                    fitness_chart=None, fitness_data=None,
                    inversion_enabled=False, elitar_percentage=5,
                    representation='binary'):
        self._population_size = population_size
        self._precision = precision
        self._epochs = epochs
        self._offspring_percentage = offspring_percentage
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._selection_method = selection_method
        self._crossover_method = crossover_method
        self._fitness_function = fitness_function
        self._mutation_method = mutation_method
        self._mutation_rate = mutation_rate
        self._elitar_strategy = elitar_strategy
        self._plot = plot
        self._fitness_chart = fitness_chart
        self._fitness_data = fitness_data
        self._inversion_enabled = inversion_enabled
        self._inversion_operator = Inversion(mutation_rate) if inversion_enabled else None
        self._elitar_percentage = elitar_percentage
        self._elitar_strategy = ElitarStrategy(elitar_percentage) if elitar_percentage > 0 else None
        self._representation = representation
        representation=representation




    def run(self):
        # Initialize objects
        #population = Population(self._population_size, self._precision)
        population = Population(
            self._population_size,
            self._precision,
            lower_bound=self._lower_bound,
            upper_bound=self._upper_bound,
            representation=self._representation
            )
        fitness_function = getattr(FitnessFunction(precision=self._precision, lower_bound=self._lower_bound, upper_bound=self._upper_bound, representation=self._representation), self._fitness_function, None)
        mutate = Mutate(self._mutation_rate)

        # Initialize 3D plot data
        x_axis = []
        y_axis = []
        z_axis = []

        # Main loop
        for epoch in range(self._epochs):
            # Evaluate population
            population_fitness = [fitness_function(chromo_value) for chromo_value in population.get_population_values()]

            # Store data for 3D plotting // x,y = zip(*[[a,b],[a,b]]) --> x = [a,a], y = [b,b]
            #x, y = zip(*[binary_to_decimal(chrom_value, self._lower_bound, self._upper_bound, self._precision) for chrom_value in population.get_population_values()])
            if self._representation == 'binary':
                decoded = [binary_to_decimal(val, self._lower_bound, self._upper_bound, self._precision)
                           for val in population.get_population_values()]
            else:
                 decoded = population.get_population_values()
            
            x, y = zip(*decoded)

            x_axis.extend(x)
            y_axis.extend(y)
            z_axis.extend(population_fitness)

            # Selection
            selection = Selection(population, population_fitness, self._offspring_percentage)
            new_population_values = getattr(selection, self._selection_method)() # Selects offspring_percentage % of population values

            # Create offspring through crossover and mutation
            offspring = new_population_values.copy()
            cycles = 1
            parents_len = len(new_population_values)

            # Calculate the amount of cycles to reach the target population, important when reproducing once is not enough
            if parents_len < self._population_size/2:
                cycles = ceil((self._population_size - parents_len)/parents_len)

            for cycle in range(cycles):
                for i in range(0, parents_len, 2):
                    # Crossover
                    #crossover = Crossover(new_population_values[i], new_population_values[i+1])
                    #child1, child2 = getattr(crossover, self._crossover_method)()
                    if self._representation == 'real':
                          from .service.real_crossover import RealCrossover
                          crossover = RealCrossover(new_population_values[i], new_population_values[i+1])
                    else:
                          from .service.crossover import Crossover
                          crossover = Crossover(new_population_values[i], new_population_values[i+1])
                    child1, child2 = getattr(crossover, self._crossover_method)()


                    # Mutate
                    #chosen_mutation_method = getattr(mutate, self._mutation_method, None)
                    #child1, child2 = chosen_mutation_method(child1), chosen_mutation_method(child2)
                    # Mutate
                    if self._representation == 'binary':
                        chosen_mutation_method = getattr(mutate, self._mutation_method, None)
                        child1, child2 = chosen_mutation_method(child1), chosen_mutation_method(child2)
                    elif self._representation == 'real':
                        if self._mutation_method == 'uniform':
                            child1 = mutate.uniform(child1)
                            child2 = mutate.uniform(child2)
                        elif self._mutation_method == 'gaussian':
                            child1 = mutate.gaussian(child1)
                            child2 = mutate.gaussian(child2)
                        else:
                            raise ValueError(f"Unsupported mutation method '{self._mutation_method}' for real representation")


                    # Apply inversion if enabled
                    if self._inversion_enabled:
                        child1 = self._inversion_operator.apply(child1)
                        child2 = self._inversion_operator.apply(child2)

                    # Add children to offspring
                    offspring.extend([child1, child2])


            # Elitar strategy
            #if self._elitar_strategy:
                #best = min(zip(population.get_population_values(), population_fitness), key=lambda x: x[1])[0]
                #if len(offspring) > 0:
                    # Replace a random offspring with the best individual
                    #offspring[random.randint(0, len(offspring) - 1)] = best
                #else:
                    #offspring.append(best)


            # Elitar strategy
            if self._elitar_strategy:
                best_individuals = self._elitar_strategy.apply(population.get_population_values(), population_fitness)
    
                for best in best_individuals:
                    if len(offspring) > 0:
                        offspring[random.randint(0, len(offspring) - 1)] = best
                    else:
                        offspring.append(best)


            # Discard the oldest chromosomes
            offspring = offspring[-self._population_size:]
            # Update population
            population.set_population(offspring)
            
            # Best fitness value for epoch
            best_fitness = min(population_fitness)
            self._fitness_data.append(best_fitness)

            # Streamlit chart actualization
            if self._fitness_chart:
                self._fitness_chart.line_chart(self._fitness_data)

        # Update plotter axis values
        if self._plot:
            self._plot.set_x_axis(x_axis)
            self._plot.set_y_axis(y_axis)
            self._plot.set_z_axis(z_axis)

        # Return the best solution
        best_solution = min(population.get_population_values(), key=fitness_function)
        return best_solution, fitness_function(best_solution)
    
    

