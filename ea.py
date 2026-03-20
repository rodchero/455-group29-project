from individual import Individual

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
        
    

