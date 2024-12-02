"""
Algoritmo de Tarjan (AP)

"""

from sys import stdin

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

def main():
    global G, n
    
    n, m = map(int, stdin.readline().split())

    for i in range(m):
        u, v = map(int, stdin.readline().split())
        G[u].append(v)
        G[v].append(u)

    ap()

    if len(apNodos) == 0:
        print("No hay puntos de articulacion")
    else:
        print("Puntos de Articulacion:")
        print(*apNodos)

main()