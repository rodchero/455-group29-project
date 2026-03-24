import random
import math

MUTATION_STRATEGY = 0
DISTANCE_RADIUS_SIGMA = 1.0

class Individual:
    '''Class which represents an individual in the population, encoding the locations of different building categories in a city layout.'''
    def __init__(self, schema, city):
        self.genes = []
        self.schema = schema
        self.offsets = {}
        self.city = city
        
        current_index = 0
        for service, count in schema.items():
            # this is to store where each building category starts and ends
            self.offsets[service] = (current_index, current_index + count)
            
            # randomly fill the list with coordinates
            for _ in range(count):
                self.genes.append((random.randint(0, city.grid_size[1] - 1), 
                                   random.randint(0, city.grid_size[0] - 1)))
            current_index += count

    def __repr__(self):
        return f"Individual(Fit: {self.fitness_evaluation()}, Genes: {self.genes[:3]})"
    
    def get_services_of_type(self, service):
        '''
        Public method which returns a list of coordinates for all of this individual's services of a given type.
        '''
        offsets = self.offsets[service]
        return self.genes[offsets[0]:offsets[1]] # returns the sublist that just contains the services of the given type

    def fitness_evaluation(self):
        '''
        Public method to evaluate the fitness of the individual.
        '''
        # The fitness of an individual is the sum over each square in the city of the distances to each kind of service (weighted by population density)
        fitness = 0.0

        # First, loop over every grid square in the city
        for row in range(self.city.grid_size[1]):
            for col in range(self.city.grid_size[0]):
                # Then, loop over every different kind of service
                for service in self.schema:
                    # Find the minimum distance by iterating over every service of this type
                    min_distance_to_service = float("inf")
                    service_locations = self.get_services_of_type(service)
                    for service_location in service_locations:
                        # distance_to_location = abs(service_location[0] - col) + abs(service_location[1] - row) # taxicab distance
                        distance_to_location = math.sqrt((service_location[0] - col) ** 2 +(service_location[1] - row) ** 2) # euclidean distance
                        min_distance_to_service = min(min_distance_to_service, distance_to_location)
                    # The minimum distance is multiplied by the population density at this location in order to favour more densely populated areas
                    fitness += math.exp(-(min_distance_to_service ** 2) / (DISTANCE_RADIUS_SIGMA ** 2)) * self.city.population_distribution[row][col]
        return fitness
    
    def mutate(self):
        '''
        Public method for mutation, which introduces random changes to the individual's genes based on the mutation rate.
        Uses the "random increment" strategy, where a random value is added to one of the gene's coordinates.
        '''
        if MUTATION_STRATEGY == 0:
            # The index at which the mutation is happening
            index = random.randint(0, len(self.genes) - 1)
            # Create a copy of the gene at that index and increases/decreases one of its coordinates by 1
            gene = self.genes[index]
            new_gene = list(gene)
            amount_to_add = random.randint(-5, 5)
            coordinate_index = random.randint(0,1) # If 0, we are changing the x coordinate. If 1, we are changing the y coordinate
            # New gene coordinate is clamped to ensure it stays on the city grid
            new_gene[coordinate_index] = max(min(new_gene[coordinate_index] + amount_to_add, self.city.grid_size[coordinate_index] - 1), 0)
            # Finally, replace the old gene with the new one
            self.genes[index] = tuple(new_gene)
        else:
            # The index at which the mutation is happening
            index = random.randint(0, len(self.genes) - 1)
            new_gene = (random.randint(0, self.city.grid_size[0] - 1), random.randint(0, self.city.grid_size[1] - 1))
            self.genes[index] = new_gene

