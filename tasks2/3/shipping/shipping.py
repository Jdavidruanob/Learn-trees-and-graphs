"""
Jose David Ruano Burbano 8982982
Tarea 3 - shipping
Arboles y grafos 2025-1

Analisis de complejidad:
Siendo M el numero de almacenes, N el numero de conexiones entre almacenes 
y P el numero de consultas de envios:

- Construccion del grafo: O(M + N)
- Búsqueda BFS para cada consulta: O(M + N)
- Procesamiento de consultas: O(P (M + N))

En total, la complejidad es O(M + N + P (M + N)), lo que en el peor de los casos 
puede ser O(PM + PN). Sin embargo, dado que P es pequeño en comparacion con M y N, 
el termino dominante es O(M + N).
"""

import sys
from collections import deque

def bfs(graph, start, end):
    q = deque()
    visited = {}  
    distance = {}  
    ans = -1
    for warehouse in graph:
        visited[warehouse] = False
        distance[warehouse] = 0
    q.append(start)
    visited[start] = True
    
    while len(q) > 0:
        v = q.popleft()
        if v == end:
            ans = distance[v]
        for u in graph[v]:
            if not visited[u]:
                q.append(u)
                visited[u] = True
                distance[u] = distance[v] + 1
    return ans  

def main():
    t = int(sys.stdin.readline().strip())
    print("SHIPPING ROUTES OUTPUT")
    
    for case in range(1, t + 1):
        print()  
        print(f"DATA SET {case}")
        print()
        
        line = sys.stdin.readline().strip().split()
        m, n, p = int(line[0]), int(line[1]), int(line[2])
        warehouses = sys.stdin.readline().strip().split()
        graph = {w: [] for w in warehouses}
        
        for _ in range(n):
            u, v = sys.stdin.readline().strip().split()
            graph[u].append(v)
            graph[v].append(u)  
        
        for _ in range(p):
            request = sys.stdin.readline().strip().split()
            size = int(request[0])
            start, end = request[1], request[2]
            
            distance = bfs(graph, start, end)
            if distance == -1:
                print("NO SHIPMENT POSSIBLE")
            else:
                cost = size * distance * 100
                print(f"${cost}")
    print()  
    print("END OF OUTPUT")

main()