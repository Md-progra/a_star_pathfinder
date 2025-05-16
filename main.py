from grid_generator import generate_grid
from a_star import a_star
from visualize import visualize

def main():
    size = 20
    grid = generate_grid(size, obstacle_prob=0.2)
    start = (0, 0)
    end = (size - 1, size - 1)

    path = a_star(grid, start, end)

    if path:
        print("✅ Path found! Visualizing...")
        visualize(grid, path)
    else:
        print("❌ No path found. Try regenerating the grid.")

if __name__ == "__main__":
    main()
