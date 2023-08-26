# maze-path-algo

## Contributor:
👤 Luthfiyyah hanifah amari

👤 Sastiara Maulikh

Course: Design & Analysis of Algorithm


## About project

This project implementing DFS (Depth-First Search) algorithm.

In this project, there will be a maze which the program will find the path from start to target/finished using DFS algorithm. For implementing the maze, visualize, and user interface the program, we used `pyamaze` package from [MAN1986](https://github.com/MAN1986).

## Algorithm and Package Explanation

### DFS (Depth-First Search) — Algorithm used

Depth first search is a recursive algorithm for searching all the vertices of a graph. 

**A standard DFS implementation puts each vertex of the graph into one of two categories:**

1. Visited
2. Not Visited

**The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.**

**The DFS algorithm works as follows:**

1. Start by putting any one of the graph's vertices on top of a stack.
2. Take the top item of the stack and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
4. Keep repeating steps 2 and 3 until the stack is empty.

**Why we use DFS Algorithm?**

1. For finding the path
2. To test if the graph is bipartite
3. For finding the strongly connected components of a graph
4. For detecting cycles in a graph

### Package `pyamaze` — Package used

The maze generation algorithm used in the **pyamaze** module ***(Recursive Backtracker)***not just generates a random maze, but also has the information of the path from start to goal. This information is available in the attribute path of the Maze as a dictionary. The key of the path is a cell and value is also a cell representing the movement from key cell to value cell in order to reach the goal.

This Package controlling the color, position such as row, grid, cell, ect.

Code Simulation :

```python
from pyamaze import maze,agent
m=maze(20,20)
m.CreateMaze(loopPercent=50)
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})
m.run()
```

## Getting Started the project

- Install package pyamaze
    
    ```cpp
    pip install pyamaze
    ```
    
- After install package we can go trough simply generate a maze, you need to create the maze object and then apply the **CreateMaze** function. The last statement will be applying the function **run** to run the simulation. We can put or change the size of the maze just like this :

![Untitled (2)](https://github.com/luthfiyyah-a/maze-path-algo/assets/79054230/94346a82-6774-40b8-bcf7-062b2054c752)


## User Interface (Screenshot output)

From the input above, we can get an output such as:
![Untitled (1)](https://github.com/luthfiyyah-a/maze-path-algo/assets/79054230/07f7dd95-3bcf-4f97-a5f5-498bc6041a1d)

- The top-left cell is the goal of the maze and there are ways we can change the goal to any cell. Moreover, by default, a **Perfect Maze** is generated, which means all cells of the maze are accessible and there is one and only one path from any cell to the goal cell. Therefore any cell can be treated as the start cell and hence is not highlighted. Internally the last cell i.e. the last row and last column cell is set as the start cell. So, the general task will be finding the way from the bottom-right cell to the top-left cell.

## Analysis / Evaluation

In general case, The time complexity of the DFS algorithm is **O(V+E)**, where V is the number of vertices and E is the number of edges in the graph. The space complexity of the DFS algorithm is O(V). In this case, the total complexity of the DFS algorithm is O(N), where N is the number of cells in the maze. We remember advantages of DFS:

- It can find solution with examining much search space and stop once found
- takes less time to reach goal node than BFS algorithm

Disadvantage of DFS, one of which is determine of depth until search has proceeded

## Conclusion

In this project, Python data structures help us to create (generate) or solve a maze. This contribution is using the basic Python data structures (list, queue, heap, deque, stack) and the basic algorithms (BFS, DFS, Dijkstra’s) as the principle to work with a maze. To generate or solve a maze means to find its spanning tree. 

The total complexity of the given DFS algorithm is O(N), where N is the number of cells in the maze. The time complexity of O(N) indicates that the execution time of the algorithm will increase linearly with the number of cells in the maze.

In each iteration of the algorithm, we explore one cell and add one relationship to **`dfsPath`**. Therefore, the time required to traverse the entire maze depends on the number of cells present. If there are N cells in the maze, the DFS algorithm will visit each cell once, resulting in a time complexity of O(N).

Additionally, the DFS algorithm uses additional data structures such as the **`explored`**, **`frontier`**, and **`dfsPath`** arrays, which require additional space to track the explored nodes, nodes to be expanded, and the path taken during the search. The space complexity of the DFS algorithm is also O(N) because we need to store information for each cell in the maze.

Thus, the total complexity of the DFS algorithm is O(N) for both time and space, with N being the number of cells in the maze.


## References

https://www.programiz.com/dsa/graph-dfs

[https://www.javatpoint.com/depth-first-search-algorithm#:~:text=Complexity of Depth-first search,algorithm is O(V)](https://www.javatpoint.com/depth-first-search-algorithm#:~:text=Complexity%20of%20Depth%2Dfirst%20search,algorithm%20is%20O(V)).

https://www.shiksha.com/online-courses/articles/bfs-vs-dfs/#vs

https://www.youtube.com/watch?v=sTRK9mQgYuc&feature=youtu.be
