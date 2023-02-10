from queue import PriorityQueue
from pyamaze import maze,agent,COLOR,textLabel



def h(cell1,cell2):
    x1,x2 = cell1
    y1,y2 = cell2

    return abs(x1-x2) + abs(y1-y2)

def astar(m,start=None):

    if start is None:
        start=(m.rows,m.cols)

    goal = m._goal
    # start = (m.rows,m.cols)
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start,goal)

    open = PriorityQueue()
    open.put((h(start,goal),h(start,goal),start))
    apath = {}
    while open:

        curcell = open.get()[2]

        if curcell == m._goal:
            break

        for d in 'ESNW':

            if m.maze_map[curcell][d] == True:

                if d == 'E':
                    childcell = (curcell[0],curcell[1]+1)

                if d == 'W':
                    childcell = (curcell[0],curcell[1]-1)

                if d == 'N':
                    childcell = (curcell[0]-1,curcell[1])

                if d == 'S':
                    childcell = (curcell[0]+1,curcell[1])

                temp_g_score = g_score[curcell]+1
                temp_f_score = temp_g_score + h(childcell,goal)

                if temp_f_score < f_score[childcell]:
                    g_score[childcell] = temp_g_score
                    f_score[childcell] = temp_f_score
                    open.put((temp_f_score,h(childcell,goal),childcell))
                    apath[childcell] = curcell
    fwpath = {}
    cell = m._goal
    while cell != start:
        fwpath[apath[cell]] = cell
        cell = apath[cell]

    return fwpath


def Accumulate_Path_Function(path):


    strPath = ''
    for k,v in path.items():

        strPath = strPath + f'{v}'

    return strPath

if __name__ == '__main__':
    m = maze(5,6)
    m.CreateMaze(x=5, y=6, loadMaze='/D:/guddu/londonmet/Artificial Intelligence/assignment.csv')

    # path,c = dijkstra(m,start=(6,1))
    path = astar(m,start=(1,1))
    strPath = Accumulate_Path_Function(path)

    print(f'Path Followed by an agent: {strPath}')
    # print(strPath)

    textLabel(m,'Total Cost',strPath)

    a = agent(m,1,1,footprints=True)

    m.tracePath({a:path})
    m.run()

