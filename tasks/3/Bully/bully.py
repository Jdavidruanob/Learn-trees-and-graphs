"""
Jose David Ruano Burbano
Parcial 1 - Parte practica - Bully
Arboles y grafos 2024-2
Universidad Pontificia Javeniana cali

"""
import sys
from collections import deque

def get_results(G):
    """ Recorre el grafo con el metodo BFS y asigna el rango a cada nodo"""
    vis = [False for _ in range(len(G))] # Nodos visitados
    rank = [-1 for _ in range(len(G))] # Rango de cada nodo
    in_degree = [0 for _ in range(len(G))] # grado de incidencia de cada nodo
    queue = deque() 
    result = []
    
    # Obtener el grado de incidencia de cada nodo
    for u in range(len(G)):
        for v in G[u]:
            in_degree[v] += 1
    
    # Inicializamos la cola con los nodos que tengan grado de incidencia 0 (jefes)
    for i in range(len(G)):
        if in_degree[i] == 0:
            queue.append((i, 1))  # (nodo, rango)
            vis[i] = True
    
    # Recorremos la cola y asignamos el rango a cada nodo
    while len(queue) > 0:
        u, r = queue.popleft() 
        rank[u] = r # asignamos el rango al nodo
        result.append((r, u))
     
        for v in G[u]: 
            if not vis[v]: 
                in_degree[v] -= 1 
                if in_degree[v] == 0: 
                    queue.append((v, r + 1))  
                    vis[v] = True 
    
    # ordenar la lista de resultados por rango y luego por nodo
    result.sort()
    return result

def main():
    t = int(sys.stdin.readline().strip())
    i = 1
    while i <= t:
        # lecturae de la entrada
        line = sys.stdin.readline().split()
        n, r = int(line[0]), int(line[1])
        graph = [[] for _ in range(n)] #  lista adyacencia

        # leer grafo
        for _ in range(r):
            relation = sys.stdin.readline().split() 
            r1, r2 = int(relation[0]), int(relation[1]) 
            graph[r2].append(r1) 

        ranked_nodes = get_results(graph)

        # imprimir salida
        print(f"Scenario #{i}:")
        for rank, node in ranked_nodes:
            print(f"{rank} {node}")
        
        i += 1


main()