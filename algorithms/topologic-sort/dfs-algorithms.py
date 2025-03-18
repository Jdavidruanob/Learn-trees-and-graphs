from collections import deque

# Ordenes topologicos usando DFS 

""" 
    Orden topológico con DFS: Versión 1
    Se registra el tiempo de finalización y después del DFS se ordenan los nodos
    por tiempo de finalización de mayor a menor
    Complejidad: T(n, m) E O(n * log n)
"""
def topoSortAux(u, G, vis):
  global t
  vis[u] = True
  t += 1
  desc[u] = t

  for w in G[u]:
    if not vis[w]:
      topoSortAux(w, G, vis)

  t += 1
  fin[u] = t

def topoSortDFS(G):
  global t, desc, fin, tree
  vis = [False for _ in range(len(G))]
  desc, fin = [None for _ in range(len(G))], [None for _ in range(len(G))]
  tree = [None for _ in range(len(G))]
  t = 0
  for u in range(len(G)):
    if not vis[u]:
      topoSortAux(u, G, vis)
  tmp = []
  for u in range(len(G)):
    tmp.append((u, fin[u]))
# se ordena respecto al segundo elemento y descendiente
  tmp.sort(key = lambda x: x[1], reverse = True) 
  topo = [u for u,_ in tmp]
  return topo

"""
    Orden topológico con DFS: Versión 2
    No se registra el tiempo de finalización pero después de finalizar cada nodo
    este es agregado a una lista. El orden topológico es esa lista pero al reves.
    Complejidad: T(n, m) E O(n + m)
"""
def topoSortAux2(u, G, vis, topo):
  global t
  vis[u] = True
  for w in G[u]:
    if not vis[w]:
      topoSortAux2(w, G, vis, topo)
  topo.append(u)
  
def topoSortDFS2(G):
  global t, desc, fin, tree
  vis = [False for _ in range(len(G))]
  t, topo = 0, deque()
  for u in range(len(G)):
    if not vis[u]:
      topoSortAux2(u, G, vis, topo)
  topo.reverse()
  return topo

"""
    Orden topológico con DFS: Versión 3
    No se registra el tiempo de finalización pero después de finalizar cada nodo
    este es agregado a una lista doblemente enlazada en el frente.
    Complejidad: T(n, m) E O(n + m)
"""
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