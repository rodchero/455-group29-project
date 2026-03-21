from individual import Individual
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from PIL import Image

'''Class which implements the evolutionary algorithm for optimizing city layouts.'''
class EA:

        
    '''Constructor for the EA class, initializing parameters and internal state.'''
    def __init__(self, population_size, max_generations, mutation_rate, schema, city):
        # parameters for the evolutionary algorithm
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.city = city

        # internal state of the algorithm
        self.population = []
        self.__initialize_population(schema)

    def visualize_population(self, num_individuals=1):
        '''
        Public method for visualizing the best n individuals in the EA, in order to monitor progress.
        '''
        # First, validate input
        if num_individuals > self.population_size:
            num_individuals = self.population_size
        # Then display a plot for each of the n individuals
        for individual in self.population[:num_individuals]: # assumes population is sorted
            plt.imshow(self.city.population_distribution, cmap="gray_r") # displays the city population density as a background
            for i, service in enumerate(individual.offsets):
                # Displays a circle at each service's location
                for service_location in individual.get_services_of_type(service):
                    # Sets up the circle image
                    circle_img = Image.open("images/circle.png").convert("RGBA")
                    circle_img_array = np.asarray(circle_img).copy()
                    
                    # Recolours the circle image
                    service_color = mpl.colormaps['tab10'].colors[i]
                    for channel in range(3):
                        circle_img_array[:, :, channel] = service_color[channel] * 255
                    circle_img = Image.fromarray(circle_img_array, "RGBA")

                    x_start = service_location[0] - 0.4
                    x_end = service_location[0] + 0.4
                    y_start = service_location[1] - 0.4
                    y_end = service_location[1] + 0.4
                        
                    plt.imshow(circle_img, extent=(x_start, x_end, y_start, y_end), aspect="equal", origin="lower") # Overlays the circle on the image
            plt.imshow([[]], extent=(-0.5, 9.5, 9.5, -0.5)) # Changes the extent to the entire image
            plt.show()

            

    '''
    Private method to initialize the population.
    This method generates an initial population of individuals randomly.
    '''
    def __initialize_population(self, schema):
        for _ in range(self.population_size):
            self.population.append(Individual(schema, self.city))
        return
    
    '''
    Private method for parent selection, which selects individuals based on their fitness.
    Uses the "tournament selection" strategy, where a subset of individuals is randomly chosen and the best among them is selected as a parent.
    '''
    def __parent_selection(self):
        #TODO
        return

    '''
    Private method for survivor selection, which determines which individuals survive to the next generation.
    Uses the "mu + lambda" selection strategy, where both parents and offspring compete for survival.
    '''
    def __survivor_selection(self, pop):
        #TODO
        return

    '''
    Private method for mutation, which introduces random changes to an individual's genes based on the mutation rate.
    Uses the "random increment" strategy, where a random value is added to one of the gene's coordinates.
    '''
    def __mutate(self, individual):
        #TODO        
        return

    '''
    Private method for recombination, which combines the genes of two parent individuals to create offspring.
    Uses a version of the "cut and crossfill" strategy.
    '''
    def __recombine(self, parent1, parent2):
        #TODO
        return
    
    '''
    Public method to run the evolutionary algorithm, which iteratively evolves the population over a specified number of generations.
    The "hard part" of this assignment.
    '''
    def run(self):
        #TODO
        return
        
    

