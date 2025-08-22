# moves (8 sides)
moves = [(-1,-1),(-1,0),(-1,1),
         (0,-1),       (0,1),
         (1,-1),(1,0),(1,1)]

# heuristic distance
def h(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

# check move valid
def ok(x,y,n,grid,vis):
    if x>=0 and x<n and y>=0 and y<n:
        if grid[x][y]==0 and vis[x][y]==0:
            return True
    return False

# Best First Search
def bfs(grid):
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1,[]

    vis=[[0]*n for i in range(n)]
    q=[[0,0,[(0,0)]]]

    while len(q)>0:
        # find min h
        best=0
        for i in range(1,len(q)):
            if h(q[i][0],q[i][1],n-1,n-1) < h(q[best][0],q[best][1],n-1,n-1):
                best=i

        x,y,path=q.pop(best)
        vis[x][y]=1

        if x==n-1 and y==n-1:
            return len(path),path

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if ok(nx,ny,n,grid,vis):
                q.append([nx,ny,path+[(nx,ny)]])

    return -1,[]

# A* Search
def astar(grid):
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1,[]

    vis=[[0]*n for i in range(n)]
    q=[[0,0,0,[(0,0)]]]  # x,y,g,path

    while len(q)>0:
        # find min f
        best=0
        for i in range(1,len(q)):
            f1=q[i][2]+h(q[i][0],q[i][1],n-1,n-1)
            f2=q[best][2]+h(q[best][0],q[best][1],n-1,n-1)
            if f1<f2:
                best=i

        x,y,g,path=q.pop(best)
        vis[x][y]=1

        if x==n-1 and y==n-1:
            return len(path),path

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if ok(nx,ny,n,grid,vis):
                q.append([nx,ny,g+1,path+[(nx,ny)]])

    return -1,[]


# testing
g1=[[0,1],[1,0]]
g2=[[0,0,0],[1,1,0],[1,1,0]]
g3=[[1,0,0],[1,1,0],[1,1,0]]

for g in [g1,g2,g3]:
    l1,p1=bfs(g)
    l2,p2=astar(g)
    print("Grid:",g)
    print("BFS greedy len:",l1,"path:",p1)
    print("A* len:",l2,"path:",p2)
    print()

/*
OUTPUTS:-
Grid: [[0, 1], [1, 0]]
BFS greedy len: 2 path: [(0, 0), (1, 1)]
A* len: 2 path: [(0, 0), (1, 1)]

Grid: [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
BFS greedy len: 4 path: [(0, 0), (0, 1), (1, 2), (2, 2)]
A* len: 4 path: [(0, 0), (0, 1), (1, 2), (2, 2)]

Grid: [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
BFS greedy len: -1 path: []
A* len: -1 path: []
*/
