from sys import stdin
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs_aux(u, G, vis):
    vis[u] = True
    print(u, end=" ")

    for w in G[u]:
        if not vis[w]:
            dfs_aux(w, G, vis)

def dfs(u, G):
    # Hacer DFS desde el nodo inicial
    vis = {key: False for key in G}
    dfs_aux(u, G, vis)
    print()

def main():
    t = int(stdin.readline().strip())
    while t != 0: 
        G = defaultdict(list) # grafo
        degree = defaultdict(int) # grados de adyacencia

        # leer grafo y obtener grado de adyacencia
        for _ in range(t):
            c1, c2 = map(int, stdin.readline().strip().split())
            G[c1].append(c2)
            G[c2].append(c1)
            degree[c1] += 1
            degree[c2] += 1

        # buscar las ciuidades de los extremos
        ends = []
        for node, deg in degree.items():
            if deg == 1:
                ends.append(node)

        # saber en que nodo vamos a iniciar (el menor de los nodos con grado 1)
        u = min(ends)

        dfs(u, G)
        t = int(stdin.readline().strip())
main()