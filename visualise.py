import matplotlib.pyplot as plt
import numpy as np

def visualize(grid, path):
    display = np.copy(grid)

    for (y, x) in path:
        if display[y][x] != -1:  # Don’t overwrite obstacles
            display[y][x] = 99  # Arbitrary high number to show path

    plt.imshow(display, cmap='viridis')
    plt.title("A* Pathfinding Result")
    plt.colorbar(label='Cell Cost')
    plt.show()
