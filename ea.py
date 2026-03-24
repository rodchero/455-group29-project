from individual import Individual
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Patch
import numpy as np
import random
import math
import copy
from PIL import Image

DISPLAY_EVERY_N_GENERATIONS = 100
NUM_INDIVIDUALS_TO_DISPLAY = 9
FIT_SHARING_SIGMA = 2.0

class EA:
    '''Class which implements the evolutionary algorithm for optimizing city layouts.'''

        
    def __init__(self, population_size, max_generations, mutation_rate, schema, city):
        '''Constructor for the EA class, initializing parameters and internal state.'''
        # parameters for the evolutionary algorithm
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.city = city
        self.parent_pool_size = math.ceil(population_size / 4.0) + 1
        self.num_offspring = math.ceil(population_size / 8.0)

        # internal state of the algorithm
        self.population = []
        self.__initialize_population(schema)

    def initialize_plots(self, num_individuals=9):
        '''
        Public method which initializes the pyplot plots which will display the city visualization.
        '''
        num_rows = int(math.sqrt(num_individuals))
        num_cols = math.ceil((num_individuals / num_rows))
        _, axs = plt.subplots(num_rows, num_cols)
        return axs


    def visualize_population(self, axs, num_individuals=9, pause_execution=False):
        '''
        Public method for visualizing the best n individuals in the EA, in order to monitor progress.
        '''
        # First, validate input
        if num_individuals > self.population_size:
            num_individuals = self.population_size
        # Then sort the population by fitness
        fitness_scores = self.__get_fitnesses(self.population)
        self.population.sort(key=(lambda individual: fitness_scores[individual]), reverse=True)
        
        # add all the urban planning elements to the legend
        legend_elements = [
            Patch(facecolor=mpl.colormaps['tab10'].colors[i], label=name)
            for i, name in enumerate(self.population[0].schema)
        ]
        fig = axs.flat[0].get_figure()
        fig.legends.clear() # prevents plots from shrinking with every generation

        # Then display a plot for each of the best n individuals
        for individual_index, individual in enumerate(self.population[:num_individuals]):
            ax = axs.flat[individual_index]
            ax.cla()
            ax.set_axis_off()
            ax.set_title(f"Fitness: {fitness_scores[individual]:.2f}", fontsize=8)
            ax.imshow(self.city.population_distribution, cmap="gray_r") # displays the city population density as a background
            for service_index, service in enumerate(individual.schema):
                # Displays a circle at each service's location
                for service_location in individual.get_services_of_type(service):
                    # Sets up the circle image
                    circle_img = Image.open("images/circle.png").convert("RGBA")
                    circle_img_array = np.asarray(circle_img).copy()
                    
                    # Recolours the circle image
                    service_color = mpl.colormaps['tab10'].colors[service_index]
                    for channel in range(3):
                        circle_img_array[:, :, channel] = service_color[channel] * 255
                    circle_img = Image.fromarray(circle_img_array, "RGBA")

                    x_start = service_location[0] - 0.4
                    x_end = service_location[0] + 0.4
                    y_start = service_location[1] - 0.4
                    y_end = service_location[1] + 0.4
                        
                    ax.imshow(circle_img, extent=(x_start, x_end, y_start, y_end), aspect="equal", origin="lower") # Overlays the circle on the image
            ax.imshow([[]], extent=(-0.5, self.city.grid_size[0] - 0.5, self.city.grid_size[1] - 0.5, -0.5)) # Resets the extent to the entire image
        
        # add the legend
        fig.legend(handles=legend_elements, loc='center right', bbox_to_anchor=(0.98, 0.5))
        fig.subplots_adjust(right=0.75)

        plt.show(block=pause_execution)
        plt.pause(0.01)

    def __initialize_population(self, schema):
        '''
        Private method to initialize the population.
        This method generates an initial population of individuals randomly.
        '''
        for _ in range(self.population_size):
            self.population.append(Individual(schema, self.city))
    
    def __get_fitnesses(self, pool):
        '''
        Private method which sorts the given population pool in-place, taking into account a solution's:
            * True fitness: the distance from each city square to the nearest of each type of service, weighted by the population density of that square.
            * Fitness sharing: a solution is penalized for being similar to other solutions
        Returns an dictionary where keys are individuals and values are their fitnesses calculated as a combination of true fitness and fitness sharing.
        '''
        fitness_values = {}

        for individual in pool:
            true_fitness = individual.fitness_evaluation()
            fitness_sharing_amount = 0.0
            # Does a naive fitness sharing calculation. Note that this operates on the genotype, not the phenotype. Genotypically, two services of the same type 
            # are completely different, whereas phenotypically they are undistinguishable (since a city only cares that a school is nearby, not which one).
            # This phenotypical understanding is what is used during fitness evaluation, but it is acceptable to use the genotypical understanding
            # for this naive fitness sharing calculation since the goal is just to curb the size of a species.
            for other in pool:
                genotype_distance = 0.0
                for i, gene in enumerate(individual.genes):
                    other_gene = other.genes[i]
                    genotype_distance += (gene[0] - other_gene[0]) ** 2 + (gene[1] - other_gene[1]) ** 2
                genotype_distance = math.sqrt(genotype_distance)
                if genotype_distance <= FIT_SHARING_SIGMA:
                    fitness_sharing_amount += 1.0 - (genotype_distance / FIT_SHARING_SIGMA)
            fitness_values[individual] = true_fitness / fitness_sharing_amount

        return fitness_values



    def __parent_selection(self):
        '''
        Private method for parent selection, which selects individuals based on their fitness.
        Uses the "tournament selection" strategy, where a subset of individuals is randomly chosen and the best among them is selected as a parent.
        '''
        random.shuffle(self.population)
        parent_pool = self.population[:self.parent_pool_size] # gets a random subset of the population
        fitness_scores = self.__get_fitnesses(parent_pool)
        # Then, return the best individual by iterating over all individuals in the dictionary
        best_individual = list(fitness_scores.keys())[0]
        for individual in fitness_scores:
            if fitness_scores[individual] > fitness_scores[best_individual]:
                best_individual = individual
        return best_individual

    def __survivor_selection(self, offspring):
        '''
        Private method for survivor selection, which determines which individuals survive to the next generation.
        Uses the "mu + lambda" selection strategy, where both parents and offspring compete for survival.
        '''
        # Combines the existing population and offspring together into one population
        mu = len(self.population)
        combined_population = self.population + offspring
        # Returns a random subset of the combined population with size equal to the size of the original population
        random.shuffle(combined_population)
        return combined_population[:mu] 

    def __recombine(self, parent1, parent2):
        '''
        Private method for recombination, which combines the genes of two parent individuals to create offspring.
        Uses a version of the "cut and crossfill" strategy.
        '''
        child = Individual(parent1.schema, parent1.city)

        start_index = random.randint(0, len(parent1.genes) - 1)
        end_index = random.randint(0, len(parent1.genes) - 1)

        if start_index > end_index:
            start_index, end_index = end_index, start_index
        
        child.genes = copy.copy(parent1.genes)
        child.genes[start_index:end_index] = parent2.genes[start_index:end_index]

        return child
    
    def run(self):
        '''
        Public method to run the evolutionary algorithm, which iteratively evolves the population over a specified number of generations.
        The "hard part" of this assignment.
        '''
        # The population is already initialized in the constructor.

        axs = self.initialize_plots(NUM_INDIVIDUALS_TO_DISPLAY)

        for generation in range(self.max_generations + 1):
            offspring = []
            for _ in range(self.num_offspring):
                parent1 = self.__parent_selection()
                parent2 = self.__parent_selection()
                child = self.__recombine(parent1, parent2)
                if random.random() < self.mutation_rate:
                    child.mutate()
                offspring.append(child)
            self.population = self.__survivor_selection(offspring)
            if generation % DISPLAY_EVERY_N_GENERATIONS == 0:
                print(f"GENERATION {generation}")
                self.visualize_population(axs, NUM_INDIVIDUALS_TO_DISPLAY, pause_execution=(generation == self.max_generations))
