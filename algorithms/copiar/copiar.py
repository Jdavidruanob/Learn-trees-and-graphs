"""DFS - BFS"""
# Recorrido dfs obteniendo los tiempos de descubrimiento y finalizacion de cada nodo

def dfsAux(G, u, vis):
    global t, desc, fin
    vis[u] = True
    t += 1
    desc[u] = t
    for v in G[u]:
        if not vis[v]:
            tree[v] = u
            dfsAux(G, v, vis)
    t += 1
    fin[u] = t
            
def dfs(G, u):
    global t, desc, fin, tree
    t = 0
    vis = [False for _  in range(G)]
    desc = [None for _ in range(G)]
    fin = [None for _ in range(G)]
    tree = [None for _ in range(G)]
    for u in range(len(G)):
        if not vis[u]:
            dfsAux(G, u, vis)


# Recorrido bfs calculando desc fin y tree
from collections import deque
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


"""TOPO SORT"""

# kahn

def topoSortKahn(G):
  inc, queue, topo = [0 for _ in range(len(G))], deque(), []
  for u in range(len(G)):
    for v in G[u]:
      inc[v] += 1
  for u in range(len(G)):
    if inc[u] == 0:
      queue.append(u)
  while len(queue) > 0:
    u = queue.popleft()
    topo.append(u)
    for v in G[u]:
      inc[v] -= 1
      if inc[v] == 0:
        queue.append(v)

  if len(topo) == len(G): ans = topo
  else: ans = []
  return ans


# Usando deque

def topoSortAux3(u, G, vis, topo):
  global t
  vis[u] = True
  for w in G[u]:
    if not vis[w]:
      topoSortAux3(w, G, vis, topo)
  topo.appendleft(u)
  
def topoSortDFS3(G):
  global t, desc, fin, tree
  vis = [False for _ in range(len(G))]
  t, topo = 0, deque()
  for u in range(len(G)):
    if not vis[u]:
      topoSortAux3(u, G, vis, topo)
  return topo

"""SCC"""

# kosaraju

def dfs1(graph, u, visited, order):
    """ Primer dfs para ordenar los nodos segun su tiempo de finalizacion """
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(graph, v, visited, order)
    order.append(u)

def dfs2(graphT, u, sccInd, num):
    """ Segundo dfs para asignar el indice de el componente fuertemente conexo """
    sccInd[u] = num
    for v in graphT[u]:
        if sccInd[v] == -1:
            dfs2(graphT, v, sccInd, num)

def kosaraju(graph, graphT):
    """ Algoritmo de Kosaraju para encontrar los componentes fuertemente conexos """
    visited = [False for _ in range(len(graph) + 1)]
    sccInd = [-1 for _ in range(len(graph) + 1)]
    order = []

    for i in range(1, len(graph) + 1):
        if not visited[i]:
            dfs1(graph, i, visited, order)

    num = 0
    order.reverse()
    for u in order:
        if sccInd[u] == -1:
            dfs2(graphT, u, sccInd, num)
            num += 1
    return sccInd

# gabow

MAX = 10000
adj = [[] for i in range(MAX)]
visitado = [0 for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC = int(), 0, 0
sccNodos, pilaS, pilaP = [], [], []

def gabow():
    for i in range(n):
        sccInd[i], visitado[i] = -1, -1

    for i in range(n):
        if visitado[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC
    t += 1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        print("SCC con indice %d: " % numSCC, end = '')
        while pilaS[-1] != v:
            a = pilaS.pop()
            print("%d " % a, end = '')
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        a = pilaS.pop()
        print("%d " % a)
        sccInd[a] = numSCC - 1
        sccNodos[numSCC - 1].append(a)
        pilaP.pop()


# tarjan



# tarjan AP

G = [[] for _ in range(50000)]
visited = [-1 for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
apNodos = set()
t, n = 0, 0

def ap():
    global low, visited, p, t
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if visited[i] == -1:
            numHijos = 0
            apAux(i, numHijos)

def apAux(v, numHijos):
    global low, visited, p, apNodos, t
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            numHijos += 1
            p[w] = v
            apAux(w, numHijos)
            low[v] = min(low[v], low[w])

            # Verificar si es un punto de articulacion
            if p[v] != -1 and low[w] >= visited[v]:
                apNodos.add(v)
                
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

    if p[v] == -1 and numHijos > 1:
        apNodos.add(v)


# tarjan bridges

G = [[] for _ in range(50000)]
visited = [False for _ in range(50000)]
low = [-1 for _ in range(50000)]
p = [-1 for _ in range(50000)]
bridgesSet = set()
t, n = int(), int()

def bridgesTarjan():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if visited[i] == -1:
            bridgesAux(i)

def bridgesAux(v):
    global low, visited, p, bridgesSet, t
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            p[w] = v
            bridgesAux(w)
            low[v] = min(low[v], low[w])

            #verificar si es un puente
            if low[w] > visited[v]:
                bridgesSet.add((v, w))
                
        elif w != p[v]:
            low[v] = min(low[v], visited[w])


"""SSSP"""

# bellmand 
INF = float("inf")
def bellmanFordMoore(G, s, dist):
    N = len(G)
    dist, pred = [INF for _ in range(N)], [-1 for _ in range(N)]
    dist[s] = 0

    i = 0
    updated = True
    while i < N - 1 and updated:
        updated = False
        for u in range(N):
            for (v, duv) in G[u]:
                if dist[u] + duv < dist[v]:
                    dist[v] = dist[u] + duv
                    pred[v] = u
                    updated = True
        i += 1

    u, ans = 0, False
    while u < N and not ans:
        j = 0
        while j < len(G[u]) and not ans:
            v, duv = G[u][j]
            if dist[u] + duv < dist[v]:
                ans = True
            j += 1
        u += 1
    return ans

def bellmanFordDetCic(G, s, dist):
    N, ciclo = len(G), []
    dist, pred = [float('inf') for _ in range(N)], [-1 for _ in range(N)]
    dist[s] = 0

    for i in range(N):
        t = -1
        for u in range(len(G)):
            for (v, duv) in G[u]:
                if dist[v] > dist[u] + duv:
                    dist[v], pred[v] = dist[u] + duv, u
                    t = v

    if t != -1:
        for i in range(N):
            t = pred[t]
            cur, ciclo = t, []
        while cur != t or len(ciclo) == 0:
            ciclo.append(cur)
            cur = pred[cur]
    return ciclo



