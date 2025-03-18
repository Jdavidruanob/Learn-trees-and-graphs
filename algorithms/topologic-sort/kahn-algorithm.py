from collections import deque
""" 
    Orden topológico con BFS (Algoritmo de Kahn)
    Se obtiene el grado de incidencia de cada nodo y se agregan a una cola
    los nodos que tienen incidencia 0. Luego, para cada elemento que se saca
    de la cola se procesan sus elementos adyacentes y se les resta 1 en su grado
    de incidencia. Se agregan los nodos a la cola a medida que su incidencia pasa
    a ser 0.
    Complejidad: T(n, m) E O(n + m)
"""

def topo_sort_kahn(G):
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