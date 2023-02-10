from numpy import true_divide
from pyamaze import maze, agent, textLabel
from queue import PriorityQueue
def h(cell1, cell2):  # distance between current and goal cell
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
def aStar(m):
    aPath = {}
    fwdPath = {}
    start = (m.rows, m.cols)
    goal = (1, 1)
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)
    open = PriorityQueue()
    open.put(((h(start, goal) + 0, h(start, goal), start)))
    while not open.empty():
        currCell = open.get()[2]
        if currCell == goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][
                d] == True:
                if d == 'E':
                    childCell = (
                    currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1,
                                 currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, goal)
                if temp_f_score < f_score[
                    childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, goal), childCell))
                    aPath[childCell] = currCell
    cell = goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return aPath
if __name__ == '__main__':
    m = maze(5, 6)
    m.CreateMaze(x=5, y=6, loadMaze='maze--2022-11-17--15-20-33.csv')
    path = aStar(m)
    print(path)
    a = agent(m, 1, 1, footprints=True)
    m.tracePath({a: path})
    m.run()