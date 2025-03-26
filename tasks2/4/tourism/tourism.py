"""
    Jose David Ruano Burbano 8982982
    Tarea 4 - tourism
    Arboles y grafos 2025-1

    Análisis de Complejidad:
    Siendo n el número de ciudades y m el número de carreteras (aristas):

    - Algoritmo de Gabow para encontrar sccs O(n + m):
    - Construcción del grafo de sccs O(n + m):
    - Selección de capitales para cada scc O(n):
    - Construcción del grafo entre capitales O(n + m):
    - Ordenamiento topológico con heap:
        * Cálculo de grados de entrada: O(n + m)
        * insertar y extraern de la cola de prioridad: O(n log n)

    ASi, la complejidad del algoritmo seria algo asi como O(n log n + m).
"""


from sys import stdin
from collections import defaultdict
import heapq

def gabow_aux(v, graph, vis, scc_ind, pila_s, pila_p, t, num_scc, sccs):
    """ Función auxiliar de Gabow para encontrar SCCs recursivamente. """
    t[0] += 1
    vis[v] = t[0]
    pila_s.append(v)
    pila_p.append(v)

    for w in graph[v]:
        if vis[w] == -1:
            gabow_aux(w, graph, vis, scc_ind, pila_s, pila_p, t, num_scc, sccs)
        elif scc_ind[w] == -1:
            while vis[pila_p[-1]] > vis[w]:
                pila_p.pop()

    if v == pila_p[-1]:
        scc = []
        num_scc[0] += 1
        while pila_s[-1] != v:
            w = pila_s.pop()
            scc.append(w)
            scc_ind[w] = num_scc[0] - 1
        w = pila_s.pop()
        scc.append(w)
        scc_ind[w] = num_scc[0] - 1
        pila_p.pop()
        sccs.append(scc)

def gabow(n, graph):
    """ Algoritmo de Gabow para encontrar las componentes fuertemente conexas. """
    vis = [-1] * n
    scc_ind = [-1] * n
    pila_s, pila_p = [], []
    t, num_scc = [0], [0]
    sccs = []

    for i in range(n):
        if vis[i] == -1:
            gabow_aux(i, graph, vis, scc_ind, pila_s, pila_p, t, num_scc, sccs)

    return sccs, scc_ind

def sort(graph, nodes, get_key):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    heap = []
    for node in nodes:
        if in_degree[node] == 0:
            heapq.heappush(heap, (get_key(node), node))
    
    result = []
    while heap:
        _, u = heapq.heappop(heap)
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, (get_key(v), v))
    
    return result

def capital_key(id, cities):
    """Retorna la clave de ordenamiento para una ciudad capital."""
    return (cities[id][1], cities[id][0])

def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        n, m = map(int, stdin.readline().split())  
        cities = []
        city_index = {} 
        index_to_name = {}  

        for i in range(n):
            name, year = stdin.readline().split()
            year = int(year)
            cities.append((name, year))
            city_index[name] = i
            index_to_name[i] = name

        graph = defaultdict(list)
        for _ in range(m):
            c1, c2 = stdin.readline().split()
            graph[city_index[c1]].append(city_index[c2])

        sccs, scc_ind = gabow(n, graph)

        capitals = []
        scc_to_capital = {}
        
        # Determinar la capital de cada scc (estado)
        for i, scc in enumerate(sccs):
            min_year = float('inf')
            candidates = []
            
            for city_id in scc:
                city_year = cities[city_id][1]
                if city_year < min_year: 
                    min_year = city_year
                    candidates = [city_id]
                elif city_year == min_year:
                    candidates.append(city_id)
            
            capital_id = min(candidates, key=lambda x: cities[x][0])
            capitals.append(capital_id)
            scc_to_capital[i] = capital_id

        # Construir grafo de sccs
        scc_graph = defaultdict(set)
        for u in range(n):
            for v in graph[u]:
                if scc_ind[u] != scc_ind[v]:  
                    scc_graph[scc_ind[u]].add(scc_ind[v])

        # Construir grafo entre capitales (ciudades capitales)
        capital_graph = defaultdict(set)
        for scc_i, neighbors in scc_graph.items():
            capital_i = scc_to_capital[scc_i]
            for scc_j in neighbors:
                capital_j = scc_to_capital[scc_j]
                capital_graph[capital_i].add(capital_j)

        capital_ids = set(capitals)
        ordered_capitals = sort(capital_graph, capital_ids, lambda id: capital_key(id, cities))

        result = [index_to_name[id] for id in ordered_capitals]
        print(" ".join(result))

main()
