from pyamaze import maze, agent, COLOR

def DFS(m):
    start = (m.rows, m.cols)
    explored=[start] # array that save node that has explored (visited)
    frontier=[start] #stack that save node that want to expand
    dfsPath={} # to record the path
    while len(frontier)>0:
        currCell = frontier.pop()
        if currCell == (1,1):
            break
        # E -> east 
        # S -> South
        # N -> North
        # W -> West
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E': 
                    childCell = (currCell[0], currCell[1]+1)
                elif d=='W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d=='S':
                    childCell = (currCell[0]+1, currCell[1])
                elif d=='N':
                    childCell = (currCell[0]-1, currCell[1])
                
                if childCell in explored:
                    continue
                
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath={}
    cell = (1,1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath

               
x = int(input('Enter width of maze: '))
y = int(input('Enter height of maze: '))
m=maze(x,y)
m.CreateMaze()
path = DFS(m)
a=agent(m, footprints=True)
m.tracePath({a:path})

# print(m.maze_map)
m.run()