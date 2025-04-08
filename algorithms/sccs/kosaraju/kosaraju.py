from sys import setrecursionlimit
setrecursionlimit(100000)
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