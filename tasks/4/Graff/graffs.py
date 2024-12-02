""" Jose David Ruano Burbano
    8982982
    Arboles y grafos
    Tarea 4 - Graff
    Analisis complejidad: 

    Analisis complejidad: 
    El algoritmo implementado tiene una complejidad temporal de O(N + M), 
    donde N es el numero de nodos y M es el numero de aristas. 
    Esto se debe a que las operaciones principales 
    incluyen la inicializacion de listas, la lectura del grafo y 
    la construccion de la lista de adyacencia, 
    el uso del algoritmo de Tarjan para encontrar puentes, 
    y la ejecucion de DFS para contar componentes conexos, 
    todas las cuales tienen una complejidad donde la mas grande es de O(N + M). 
        
    """  
from sys import stdin, setrecursionlimit

# Aumentar el límite de recursión
setrecursionlimit(10**6)

# Variables globales
G = []
low = []
p = []
bridgesSet = set()
visited = []
t, n = int(), int()
count = []
id = 0

def dfsAux(v):
    global id
    visited[v] = True
    count[id] += 1
    for i in range (len(G[v])):
        u = G[v][i]
        if not visited[u] and (v, u) not in bridgesSet and (u, v) not in bridgesSet:
            dfsAux(u)

def dfs():
    global id
    for i in range(1, n + 1):
        if not visited[i]:
            id += 1
            dfsAux(i)

def bridgesAux(v):
    global low, visited, p, bridgesSet, t
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if visited[w] == -1:
            p[w] = v
            bridgesAux(w)
            low[v] = min(low[v], low[w])

            # Verificar si es un puente
            if low[w] > visited[v]:
                bridgesSet.add((v, w))
                
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

def bridgesTarjan():
    global low, visited, p
    for i in range(n + 1):
        low[i] = visited[i] = p[i] = -1

    for i in range(1, n + 1):
        if visited[i] == -1:
            bridgesAux(i)

def main():
    global G, n, visited, low, p, count, id, t
    line = stdin.readline()
    while line != "":
        n, m = map(int, line.split())

        G = [[] for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        low = [-1 for _ in range(n + 1)]
        p = [-1 for _ in range(n + 1)]
        count = [0 for _ in range(n + 1)]
        bridgesSet.clear()
        id = 0
        t = 0

        # Leer grafo
        for _ in range(m):
            u, v = map(int, stdin.readline().split())
            G[u].append(v)
            G[v].append(u)

        # Obtener los puentes del grafo
        bridgesTarjan()

        # Reiniciar visited para hacer un dfs 
        # y guardar en count el tamaño de cada componente conexo que quede despues de quitar los puentes 
        visited = [False for _ in range(n + 1)]
        dfs()

        # Obtenemos la cantidad de fallos posibles viendo cuantas parejas
        # Puedo formar con los componentes conexos que quedan sin los puentes 
        fail = 0
        for i in range(1, id + 1):
            if count[i]:
                fail += count[i] * (count[i] - 1) // 2

        # Calculamos la probabilidad de elegir una pareja que falle
        total_pairs = n * (n - 1) // 2
        result = 1.0 - (fail / total_pairs)
        print(f"{result:.5f}")

        line = stdin.readline()

main()