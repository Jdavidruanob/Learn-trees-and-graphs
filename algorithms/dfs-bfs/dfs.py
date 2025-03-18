# DFS normal
""" dfsAux
    Performs the actual dfs traversal 
    from a given node
"""
def dfsAux(G, u, vis):
    vis[u] = True
    
    for v in G[u]:
        if not vis[v]:
            dfsAux(G, v, vis)


""" dfs
    Inicializes the vis structure and ensures 
    that all nodes of graph are travesed"
    in case is it a non-connect graph     
"""
def dfs(G, u):
    
    vis = [False for _  in range(G)]
    for u in range(len(G)):
        if not vis[u]:
            dfsAux(G, u, vis)


# DFS obtaining the discovery and finishing times of each node.
def dfsAux(G, u, vis):
    global t, desc, fin
    vis[u] = True
    t += 1
    desc[u] = t
    for v in G[u]:
        if not vis[v]:
            dfsAux(G, v, vis)
    t += 1
    fin[u] = t
            
def dfs(G, u):
    global t, desc, fin
    t = 0
    vis = [False for _  in range(G)]
    desc = [None for _ in range(G)]
    fin = [None for _ in range(G)]
    for u in range(len(G)):
        if not vis[u]:
            dfsAux(G, u, vis)


# DFS obtaining the tree of travesel, that is a array who contain de father of each node
def dfsAux(G, u, vis):
    global tree
    vis[u] = True
    for v in G[u]:
        if not vis[v]:
            tree[v] = u
            dfsAux(G, v, vis)
            
def dfs(G, u):
    global tree
    tree = [None for _ in range(G)]
    vis = [False for _  in range(G)]
    for u in range(len(G)):
        if not vis[u]:
            dfsAux(G, u, vis)
            


