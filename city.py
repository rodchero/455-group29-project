import random as rng
from perlin_noise import PerlinNoise

'''Class which represents the city as a grid with population distribution.'''
class City:
    def __init__(self, grid_size=(10, 10), population_range=(0, 10), seed = 0):
        self.population_distribution = []
        self.grid_size = grid_size
        self.min_population = population_range[0]
        self.max_population = population_range[1]

        # to allow for reproducibility 
        noise = PerlinNoise(octaves=2, seed=seed)

        for x in range(grid_size[1]):
            row = []
            for y in range(grid_size[0]):
                population_density = self.min_population + noise.noise([x / grid_size[1], y / grid_size[0]]) * (self.max_population - self.min_population)
                row.append(population_density)
            self.population_distribution.append(row)
        return


    # deprecated
    def __repr__(self):
        res=""
        res+= "========"*self.grid_size[0] + "=\n"
        for row in self.population_distribution:
            for cell in row:
                res+=f"|{cell:3.{2}}\t"
            res+= "|\n" + "--------"*self.grid_size[0] + "-\n" 
        res+= "========"*self.grid_size[0] + "=\n" 
        return res
    

if __name__ == "__main__":
    print("Example city with seed=42")
    print(City(grid_size=(10, 10), seed=42))