# 🧭 A* Pathfinder on a Probabilistic Grid

This project implements the A* pathfinding algorithm over a dynamically generated grid with randomized terrain costs and obstacles. It visualizes the shortest-cost path from the top-left to the bottom-right corner, simulating decision-making under uncertainty.

---

## 🚀 Features

- ✅ Dynamic `n x n` grid generation
- 🚧 Randomly placed obstacles using a probability threshold
- 💰 Variable movement costs for each cell
- ⭐ A* algorithm using Manhattan heuristic
- 📊 Visualization of the grid and optimal path using `matplotlib`

---

## 🧠 How It Works

- **Grid Generation**: Each cell is randomly assigned a movement cost between 1 and 5. With a configurable probability, cells may become obstacles (value `-1`).
- **A\* Search**: The algorithm finds the optimal path from `(0,0)` to `(n-1,n-1)` using:
  - `g(n)`: cost so far
  - `h(n)`: Manhattan distance to the goal
  - `f(n) = g(n) + h(n)`
- **Visualization**: The final path is drawn in bright yellow. Obstacles appear darkest, and higher movement costs are brighter.

---

## 📂 Project Structure

