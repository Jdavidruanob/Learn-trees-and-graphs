# Recorrido dfs normal

def dfsAux(G, u, vis):
    vis[u] = True
    
    for v in G[u]:
        if not vis[v]:
            dfsAux(G, v, vis)
            
def dfs(G, u):
    vis = [False for _  in range(G)]

    for u in range(len(G)):
        if not vis[u]:
            dfsAux(G, u, vis)

# Recorrido dfs obteniendo los tiempos de descubrimiento y finalizacion de cada nodo

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


# Recorrido dsf obteniendo el arbol, tree que contiene los padres de cada nodo

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
            


