""" Imports needed """
from sys import stdin
from collections import deque

G = [[] for i in range (5000)]

""" Find diameter of tree n-ary """

dist_max, nodo_max = None, None # Variables necesarias 

def dfs_diameter(v, p, dist):
  global dist_max, nodo_max
  dist += 1
  if dist > dist_max: dist_max, nodo_max = dist, v
  for w in  G[v]:
    if w != p:
      dfs_diameter(w, v, dist)

def diameter():
  global dist_max
  dist_max = 0
  dfs_diameter(0, -1, -1)
  dfs_diameter(nodo_max, -1, -1)
  return dist_max


""" Find radio of tree n-ary  """

def radio():
  diam = diameter()
  radio = (diam + 1) // 2
  return radio

""" Find center of tree n-ary (calculates additionals for diameter and radio)"""

def center():
  nivelMax = 0
  nivel = [0 for _ in range(len(G))]
  grado = [len(G[v]) for v in range(len(G))]
  queue = deque()
  nodosCentro = set()

  for i in range(len(G)):
    if grado[i] == 1:
      queue.append(i)

  while len(queue) > 0:
   v = queue.popleft()
   for w in G[v]:
     grado[w] -= 1
     if grado[w] == 1:
       queue.append(w)
       nivel[w] = nivel[v] + 1
       nivelMax = max(nivelMax, nivel[w])
  for i in range(len(G)):
    if nivel[i] == nivelMax:
      nodosCentro.add(i)

  radio = nivelMax + 1 if len(nodosCentro) == 2 else  nivelMax
  if len(nodosCentro) == 2: diametro = 2 * radio - 1
  else: diametro = 2 * radio

  return radio, diametro, nodosCentro
 
