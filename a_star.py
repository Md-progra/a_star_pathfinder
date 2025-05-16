import heapq

def heuristic(a, b):
    """Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    rows, cols = grid.shape

    # Priority queue: (f_score, position)
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}  # For path reconstruction
    g_score = {start: 0}  # Cost from start to node

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            # Path found: reconstruct it
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Explore neighbors
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                # Skip obstacles
                if grid[neighbor] == -1:
                    continue

                tentative_g = g_score[current] + grid[neighbor]

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path found
