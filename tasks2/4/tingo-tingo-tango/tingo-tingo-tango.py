"""
    Jose David Ruano Burbano 8982982
    Tarea 4 - tingo-tingo-tango
    Arboles y grafos 2025-1

    Análisis de Complejidad:
    Siendo n el número de personas y m el número de relaciones de paso:

    - Construcción del grafo dirigido: O(n + m)
    - Algoritmo de Tarjan:
        * DFS para encontrar sccs: O(n + m)
    - Construcción del grafo de sccs: O(n + m)
    - BFS en el grafo condensado: O(n + m)

    En total, la complejidad es O(n + m).
"""

from sys import stdin
from collections import deque
def tarjan_scc_aux(u):
    global t, scc_count
    dis[u] = low[u] = t
    t += 1
    stack.append(u)
    in_stack[u] = True

    for v in graph[u]:
        if dis[v] == -1: 
            tarjan_scc_aux(v)
            low[u] = min(low[u], low[v])
        elif in_stack[v]:  
            low[u] = min(low[u], dis[v])

    if dis[u] == low[u]:  
        w = -1
        while w != u:
            w = stack.pop()
            in_stack[w] = False
            scc_id[w] = scc_count
        scc_count += 1

def tarjan_scc(n):
    global dis, low, scc_id, in_stack, stack, t, scc_count
    low = [-1] * (n + 1)
    dis = [-1] * (n + 1)
    scc_id = [-1] * (n + 1)
    stack = []
    in_stack = [False] * (n + 1)
    t = scc_count = 0

    for i in range(1, n + 1):
        if dis[i] == -1:
            tarjan_scc_aux(i)

def bfs(start, target, n):
    queue = deque([(start, 0)])
    visited = [False] * (n + 1)  
    visited[start] = True
    ans = -1
    
    while queue and ans == -1:
        u, dist = queue.popleft()
        if u == target:
            ans = dist
        else:
            for v in graph_scc[u]: 
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, dist + 1))
    return ans


def main():
    n, m = map(int, stdin.readline().split())
    while n != 0 and m != 0:
        global graph, graph_scc
        graph = [[] for _ in range(n+1)]
        
        z, x = map(int, stdin.readline().split())
        for _ in range(m):
            p, q = map(int, stdin.readline().split())
            graph[p].append(q)

        tarjan_scc(n)
        graph_scc = [[] for _ in range(n+1)]
        for u in range(1, n + 1):
            for v in graph[u]:
                if scc_id[u] != scc_id[v]:
                    graph_scc[scc_id[u]].append(scc_id[v])
        ans = bfs(scc_id[z], scc_id[x], n)
        print(f"Zlatan will need the object to pass through {ans} groups.")
        n, m = map(int, stdin.readline().split())

main()