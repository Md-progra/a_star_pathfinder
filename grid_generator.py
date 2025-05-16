import numpy as np
import random

def generate_grid(size, obstacle_prob= 0.2, cost_range =(1,5)):
    grid = np.random.randint(cost_range[0], cost_range[1]+1, size = (size,size))
    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_prob:
                grid[i][j] = -1
    grid[0][0] = 1
    grid[size-1][size-1] = 1

    return grid