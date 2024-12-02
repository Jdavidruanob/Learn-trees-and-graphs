"""
Tarea 6
Arboles y grafos 
Jose David Ruano Burbano 
8982982

Analisis de complejidad:
n es el número de ciudades en el imperio de Zlatan.
m es el número de carreteras entre las ciudades.

- Algoritmo de Kosaraju para encontrar los SSCs O(n + m)
- Construccion del grafo condensado no dirigido (arbol) de SSCs O(n + m)
- Calculo del centro del arbol O(n)
- Obtener estado capital y ciudad capital O(n)

Por lo tanto:
La complejidad temporal total de la solucion es O(n + m),
respecto al número de ciudades n y carreteras m del grafo.

"""
from sys import stdin
from collections import deque

def dfs1(graph, u, visited, order):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(graph, v, visited, order)
    order.append(u)

def dfs2(graphT, u, sccInd, num):
    sccInd[u] = num
    for v in graphT[u]:
        if sccInd[v] == -1:
            dfs2(graphT, v, sccInd, num)

def kosaraju(graph, graphT):
    visited = [False for _ in range(len(graph))]
    sccInd = [-1 for _ in range(len(graph))]
    order = []

    for i in range(len(graph)):
        if not visited[i]:
            dfs1(graph, i, visited, order)

    num = 0
    order.reverse()
    for u in order:
        if sccInd[u] == -1:
            dfs2(graphT, u, sccInd, num)
            num += 1
    return sccInd, num


def center(G):
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

def getCapitalSate(sccInd, centerNodes):
    ans = set()
    if len(centerNodes) == 1:
       for node in range(len(sccInd)):
          if sccInd[node] == centerNodes[0]:
             ans.add(node)
    elif len(centerNodes) == 2:
       for node in range(len(sccInd)):
          if sccInd[node] == centerNodes[0] or sccInd[node] == centerNodes[1]:
             ans.add(node)
    else:
       for node in range(len(sccInd)):
            ans.add(node)
    return ans

def getCapitalCity(capitalState, values):
    capital = list(capitalState)
    ans = capital[0]
    i = 1
    while i < len(capital):
        #print(f"node: {values[i]} ans: {values[ans]} ")
        if values[capital[i]] > values[ans]:
           ans = capital[i] 
        i+=1
    return ans
   
def main():

    n, m = map(int, stdin.readline().split())
    while n != 0 and m != 0: 
        g, values, gT = [[] for _ in range(n)], [], [[] for _ in range(n)]
        values = list(map(int, stdin.readline().split()))

        for _ in range(m):
            u, v = map(int, stdin.readline().split())
            g[u].append(v)
            gT[v].append(u)
        
        sccInd, numScc = kosaraju(g,gT)
        sccG = [[] for _ in range(numScc)]
        # Crear grafo de sccs
        for u in range(n):
            for v in g[u]:
                if (sccInd[u] != sccInd[v]):
                    sccG[sccInd[u]].append(sccInd[v])
                    sccG[sccInd[v]].append(sccInd[u])

        radio, diameter, Center = center(sccG)
        centerNodes = list(Center)
        capitalState = getCapitalSate(sccInd, centerNodes)
        capitalCity = getCapitalCity(capitalState, values)
        print(capitalCity)
        n, m = map(int, stdin.readline().split())

main()
