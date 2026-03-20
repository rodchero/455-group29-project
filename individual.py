import random
import math

'''Class which represents an individual in the population, encoding the locations of different building categories in a city layout.'''
class Individual:
    def __init__(self, schema, city):
        self.genes = []
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
        return f"Individual(Fit: {self.__fitness_evaluation()}, Genes: {self.genes[:3]})"
    
    '''
    Method which returns a list of coordinates for all of this individual's services of a given type.
    '''
    def get_services_of_type(self, service):
        offsets = self.offsets[service]
        return self.genes[offsets[0]:offsets[1]] # returns the sublist that just contains the services of the given type

    '''
    Private method to evaluate the fitness of an individual.
    '''
    def __fitness_evaluation(self):
        # The fitness of an individual is the sum over each square in the city of the distances to each kind of service (weighted by population density)
        fitness = 0.0

        # First, loop over every grid square in the city
        for row in range(self.city.grid_size[1]):
            for col in range(self.city.grid_size[0]):
                # Then, loop over every different kind of service
                for service in self.offsets:
                    # Find the minimum distance by iterating over every service of this type
                    min_distance_to_service = float("inf")
                    service_locations = self.get_services_of_type(service)
                    for service_location in service_locations:
                        # distance_to_location = abs(service_location[0] - col) + abs(service_location[1] - row) # taxicab distance
                        distance_to_location = math.sqrt((service_location[0] - col) ** 2 +(service_location[1] - row) ** 2) # euclidean distance
                        min_distance_to_service = min(min_distance_to_service, distance_to_location)
                    # The minimum distance is multiplied by the population density at this location in order to favour more densely populated areas
                    fitness -= min_distance_to_service * self.city.population_distribution[row][col]
        return fitness