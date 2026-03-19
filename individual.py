import random

'''Class which represents an individual in the population, encoding the locations of different building categories in a city layout.'''
class Individual:
    def __init__(self, schema, grid_size=100):
        self.genes = []
        self.offsets = {}
        self.fitness = 0
        
        current_index = 0
        for service, count in schema.items():
            # this is to store where each building category starts
            self.offsets[service] = current_index
            
            # randomly fill the list with coordinates
            for _ in range(count):
                self.genes.append((random.randint(0, grid_size), 
                                   random.randint(0, grid_size)))
            current_index += count

    def __repr__(self):
        return f"City(Fit: {self.fitness}, Genes: {self.genes[:3]})"