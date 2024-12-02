"""
Ejemplos Representación Implícita de Grafos
Árboles y Grafos
Agosto 27 de 2024

"""

from collections import deque

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

"""
def dfsAux(x, y, vis, mapa):
  vis[x][y] = True
  print("Nodo = (%d, %d)" % (x, y))
  if x + 1 < len(mapa) and not vis[x + 1][y]:
    dfsAux(x + 1, y, vis, mapa)
  if x - 1 >= 0  and not vis[x - 1][y]:
    dfsAux(x - 1, y, vis, mapa)
  if y + 1 < len(mapa[x]) and not vis[x][y + 1]:
    dfsAux(x, y + 1, vis, mapa)
  if y - 1 < >= 0 and not vis[x][y - 1]::
    dfsAux(x, y, vis, mapa)
"""

def dfsAux(x, y, vis, mapa):
  vis[x][y] = True
  print("Nodo = (%d, %d)" % (x, y))
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[nx]) and not vis[nx][ny]:
      dfsAux(nx, ny, vis, mapa)

def dfs(mapa, posIni):
  vis = [[False for _ in range(len(mapa[i]))] for i in range(len(mapa))]
  dfsAux(posIni[0], posIni[1], vis, mapa)


"""
def bfsAux(x, y, vis, mapa):
  q = deque()
  vis[x][y] = True
  q.append((x, y))

  while len(q) > 0:
    cx, cy = q.popleft()
    print("Nodo = (%d, %d)" % (cx, cy))

    if cx + 1 < len(mapa) and not vis[cx + 1][cy]:
      vis[cx + 1][cy] = True
      q.append((cx + 1, cy))
    if cx - 1 >= 0  and not vis[cx - 1][cy]:
      vis[cx - 1][cy] = True
      q.append((cx - 1, cy))
    if cy + 1 < len(mapa[cx]) and not vis[cx][cy + 1]:
      vis[cx][cy + 1] = True
      q.append((cx, cy + 1))
    if cy - 1 >= 0  and not vis[cx][cy - 1]:
      vis[cx][cy - 1] = True
      q.append((cx, cy - 1))
"""

def bfsAux(x, y, vis, mapa):
  q = deque()
  vis[x][y] = True
  q.append((x, y))

  while len(q) > 0:
    cx, cy = q.popleft()
    print("Nodo = (%d, %d)" % (cx, cy))
    
    for k in range(4):
      nx, ny = cx + dx[k], cy + dy[k]
      if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[nx]) and not vis[nx][ny]:
        vis[nx][ny] = True
        q.append((nx, ny))
             
def bfs(mapa, posIni):
  vis = [[False for _ in range(len(mapa[i]))] for i in range(len(mapa))]
  bfsAux(posIni[0], posIni[1], vis, mapa)
             
def main():
    mapa = [[0, 1, -1, 0, 0, 0, 0, 2],
            [0, -1, -1, 0, 0, 0, -1, 0],
            [0, 0, -1, -1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, -1, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -1, -1, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, -1, 0, 0]]
    posIni = (0, 1)
    #bfs(mapa, posIni)
    dfs(mapa, posIni)

main()
