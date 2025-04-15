"""
Jose David Ruano Burbano 8982982
Tarea 5 - Fredericton
Árboles y Grafos 2025-1

Análisis de Complejidad:
Siendo n el número de ciudades, m el número de vuelos y q el número de consultas:

- Ordenamiento topológico: O(n + m)
- Caminos mínimos en DAG con hasta n-1 escalas: O(n * m)
- Procesamiento de consultas: O(q * n)

Complejidad total por escenario: O(n * m + q * n)
"""


from sys import stdin
from collections import defaultdict, deque

INF = float("inf")

def kahn_toposort(graph, city_names):
    in_degree = {city: 0 for city in city_names}
    for u in graph:
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    queue = deque([city for city in city_names if in_degree[city] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order

def sspDAG_mod(graph, city_names, start_city, end_city, max_edges):
    topo_order = kahn_toposort(graph, city_names)
    
    cost = {city: [INF] * (max_edges + 1) for city in city_names}
    cost[start_city][0] = 0  
    
    for k in range(1, max_edges + 1):
        for u in topo_order:
            if cost[u][k-1] != INF:
                for (v, c) in graph[u]:
                    if cost[v][k] > cost[u][k-1] + c:
                        cost[v][k] = cost[u][k-1] + c
    ans = cost[end_city][1:max_edges+1]    
    return ans

def main():
    t = int(stdin.readline())
    for i in range(t):
        stdin.readline()  
        n = int(stdin.readline())
        city_names = [stdin.readline().strip() for _ in range(n)]
        m = int(stdin.readline())
        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = stdin.readline().split()
            graph[u].append((v, int(w)))
        
        parts = stdin.readline().split()
        q = int(parts[0])
        queries = list(map(int, parts[1:]))
        
        start_city = city_names[0]
        end_city = city_names[-1]
        max_possible_edges = n - 1
        
        costs = sspDAG_mod(graph, city_names, start_city, end_city, max_possible_edges)
        
        print(f'Scenario #{i + 1}')
        for stops in queries:
            allowed_edges = stops + 1  
            allowed_edges = min(allowed_edges, max_possible_edges)
            
            if allowed_edges >= 1:
                min_cost = min(costs[:allowed_edges])
                if min_cost != INF:
                    print(f"Total cost of flight(s) is ${min_cost}")
                else:
                    print("No satisfactory flights")
            else:
                print("No satisfactory flights")
        if i != t - 1:
            print()

main()