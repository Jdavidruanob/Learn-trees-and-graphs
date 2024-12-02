""" Jose David Ruano Burbano
    8982982
    Arboles y grafos
    Tarea 4 - Capital
    Analisis complejidad: 

    analisis complejidad:

    El algoritmo implementado utiliza el algoritmo de Kosaraju para encontrar los
    componentes fuertemente conexos (SCC) en un grafo dirigido. 
    La complejidad temporal del algoritmo de Kosaraju es O(N + M)
    donde N es el numero de nodos (ciudades) y M es el numero de aristas (caminos). 

    Por lo tanto, la complejidad temporal total del algoritmo es O(N + M) 
    ya que las demas partes de la tambien cumplen con esta complejidad 
    
"""  

from sys import stdin
import sys
sys.setrecursionlimit(200000)

def dfs1(graph, u, visited, order):
    """ Primer dfs para ordenar los nodos segun su tiempo de finalizacion """
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(graph, v, visited, order)
    order.append(u)

def dfs2(graphT, u, sccInd, num):
    """ Segundo dfs para asignar el indice de el componente fuertemente conexo """
    sccInd[u] = num
    for v in graphT[u]:
        if sccInd[v] == -1:
            dfs2(graphT, v, sccInd, num)

def kosaraju(graph, graphT):
    """ Algoritmo de Kosaraju para encontrar los componentes fuertemente conexos """
    visited = [False for _ in range(len(graph) + 1)]
    sccInd = [-1 for _ in range(len(graph) + 1)]
    order = []

    for i in range(1, len(graph) + 1):
        if not visited[i]:
            dfs1(graph, i, visited, order)

    num = 0
    order.reverse()
    for u in order:
        if sccInd[u] == -1:
            dfs2(graphT, u, sccInd, num)
            num += 1
    return sccInd

def main():
    line = stdin.readline()
    while line.strip():
        n, m = map(int, line.split())
        graph = [[] for _ in range(n + 1)] # grafo original
        graphT = [[] for _ in range(n + 1)] # grafo transpuesto

        # Construccion del grafo    
        for i in range(m):
            u, v = map(int, stdin.readline().split())
            graph[u].append(v)
            graphT[v].append(u)
            
        # Obtener los indices de los scc con kosaraju
        sccInd = kosaraju(n, graph, graphT)

        # Calculo del grado de adyacencia de scc
        outdegree = [0 for _ in range(max(sccInd) + 1)]
        for u in range(1, n + 1):
            for v in graph[u]:
                if sccInd[u] != sccInd[v]:
                    outdegree[sccInd[u]] += 1

        # Sera candidato a capital de la nacion los scc con grado de adyacencia 0
        candidateSCCs = []
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                candidateSCCs.append(i)

        # Solo puede haber un scc con grado de adyacencia 0
        if len(candidateSCCs) != 1: 
            print("0")
        else:
            # Obtener el scc capital
            capitalSCC = candidateSCCs[0]

            # Obtener las ciudades que pertenecen al scc capital
            candidateCities = []
            for i in range(1, n + 1):
                if sccInd[i] == capitalSCC:
                    candidateCities.append(i)

            # Ordenar las ciudades de forma ascendente
            candidateCities.sort()  

            # Imprimir salida
            print(len(candidateCities))

            for city in candidateCities:
                print(city, end=" ")
            print()

        line = stdin.readline()


main()