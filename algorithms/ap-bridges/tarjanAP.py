import sys

sys.setrecursionlimit(10**6)

def articulation_aux(v):
    global t
    t += 1
    visited[v] = True
    low[v] = disc[v] = t
    children = 0

    for w in G[v]:
        if not visited[w]:  # Si w no ha sido visitado
            p[w] = v
            children += 1
            articulation_aux(w)
            low[v] = min(low[v], low[w])

            # Caso raíz del DFS
            if p[v] == -1 and children > 1:
                articulationSet.add(v)

            # Caso general
            if p[v] != -1 and low[w] >= disc[v]:
                articulationSet.add(v)

        elif w != p[v]:  # Si es un back edge, condicion necesaria pq se define en un grafo no dirigido
            low[v] = min(low[v], disc[w])

def articulation_tarjan():
    for i in range(n):
        visited[i] = False
        low[i] = disc[i] = p[i] = -1

    for i in range(n):
        if not visited[i]:
            articulation_aux(i)

# Entrada y ejecución
if __name__ == "__main__":
    n, m = map(int, input().split())  # Número de nodos y aristas
    G = [[] for _ in range(n)]
    visited = [False] * n
    low = [-1] * n
    disc = [-1] * n
    p = [-1] * n
    articulationSet = set()
    t = 0

    for _ in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    articulation_tarjan()

    if not articulationSet:
        print("-1")
    else:
        print("Total puntos de articulación:", len(articulationSet))
        print(*sorted(articulationSet))
