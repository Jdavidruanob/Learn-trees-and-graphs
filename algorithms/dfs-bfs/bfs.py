from collections import deque
# BFS normal

def bfsAux(G, u, vis):
    queue = deque()
    vis[u] = True
    queue.append(u)

    while len(queue) > 0: # Real bfs traversal 
        u = queue.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v] = True
                queue.append(v)


def bfs(G, u):
    vis = [False for _ in range(G)]
    for node in range(len(G)): # To ensure if the graph is non-connected
        if not vis[node]:
            bfsAux[G, u, vis]


# BFS with calculated desc fin and tree

def bfsAux(G, u, vis):
    global t, desc, fin, tree
    queue = deque()
    vis[u] = True
    queue.append(u)
    t += 1
    desc[u] = 1

    while len(queue) > 0:
        u = queue.popleft()
        for v in G[u]:
            if not vis[v]:
                tree[v] = u
                vis[v] = True
                t += 1
                queue.append(v)
                desc[v] = t
        t += 1
        fin[u] = t
    
            
def bfs(G, u):
    global t, desc, fin , tree
    vis = [False for _ in range(G)]
    desc, fin, tree = [None for _ in range(G)], [None for _ in range(G)], [None for _ in range(G)]
    t = 0
    for node in range(len(G)):
        if not vis[node]:
            bfsAux[G, u, vis]