"""
Tarea 6
Arboles y grafos 
Jose David Ruano Burbano 
8982982

Analisis complejidad:
n es el número de ubicaciones en el mundo del juego.
m es el número de pasajes bidireccionales entre las ubicaciones. 

- Algoritmo de Tarjan para encontrar puentes O(n + m)
- Asignacion de componentes biconexos utilizando DFS O(n + m)
- Construccion del grafo de componentes o arbol O(m)
- Calculo del diametro del arbol de puentes O(n) donde n representa 
   el número de componentes en el arbol de puentes que es como maximo 
   el número de ubicaciones originales.

Por lo tanto:
La complejidad temporal total de la solucion es O(n + m). 
respecto al número de ubicaciones n y pasajes m del grafo.

"""
from sys import stdin

G = []
visited = []
low = []
p = []
bridgesSet = set()
t, n = int(), int()
distMax, nodoMax = -1, -1
G_diameter = None
comp = [-1 for _ in range(n)]
comp_id = int()

def bridgesTarjan():
    global low, visited, p, t, bridgesSet
    t = 0
    bridgesSet.clear()
    for i in range(n):
        low[i] = visited[i] = p[i] = -1
    for i in range(n):
        if visited[i] == -1:
            bridgesAux(i)

def bridgesAux(v):
    global low, visited, p, bridgesSet, t, G
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            p[w] = v
            bridgesAux(w)
            low[v] = min(low[v], low[w])

            # Verificar si es un puente
            if low[w] > visited[v]:
                bridgesSet.add((v, w))
                bridgesSet.add((w, v))
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

def dfsAux(v, p, dist):
    global distMax, nodoMax, G_diameter
    dist += 1
    if dist > distMax:
        distMax, nodoMax = dist, v
    for w in G_diameter[v]:
        if w != p:
            dfsAux(w, v, dist)

def diameter():
    global distMax, nodoMax
    distMax, nodoMax = 0, 0
    dfsAux(0, -1, -1)  # Primer DFS desde el nodo 0
    distMax, nodoMax = 0, nodoMax
    dfsAux(nodoMax, -1, -1)  # Segundo DFS desde el nodo mas lejano encontrado
    return distMax

def dfsComp(u, comp, comp_id):
    comp[u] = comp_id
    for v in G[u]:
        if comp[v] == -1 and (u, v) not in bridgesSet:
            dfsComp(v, comp, comp_id)

def main():
    global G, visited, low, p, bridgesSet, t, n, G_diameter
    line = stdin.readline()
    while line != "":
        n, m = map(int, line.split())
        G = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, stdin.readline().split())
            u -= 1
            v -= 1
            G[u].append(v)
            G[v].append(u)

        visited, low, p = [-1 for _ in range(n)], [-1 for _ in range(n)], [-1 for _ in range(n)]
        bridgesSet, t = set(), 0
        bridgesTarjan()

        if not bridgesSet:
            print(0)
            line = stdin.readline()
        else:
            # Asignar componentes
            comp = [-1 for _ in range(n)]
            comp_id = 0
            for i in range(n):
                if comp[i] == -1:
                    dfsComp(i, comp, comp_id)
                    comp_id += 1
            # Construir el grafo de componentes (arbol)
            G_diameter = [[] for _ in range(comp_id)]
            for u, v in bridgesSet:
                cu = comp[u]
                cv = comp[v]
                if cu != cv:
                    G_diameter[cu].append(cv)
            dia = diameter()
            print(dia)
            line = stdin.readline()

main()