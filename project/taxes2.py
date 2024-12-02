from sys import stdin

G, n = [], int() # Generales 
bridges_set, t, visited, low, p = set(), int(), [], [], [] # Para bridgesTarjan

def bridges_tarjan():
    global low, visited, p, t, bridges_set
    t = 0
    bridges_set.clear()
    for i in range(n):
        low[i] = visited[i] = p[i] = -1
    for i in range(n):
        if visited[i] == -1:
            bridges_aux(i)

def bridges_aux(v):
    global low, visited, p, bridges_set, t, G
    t += 1
    visited[v] = low[v] = t

    for pair in G[v]:
        w = pair[0] # Referirse a v en (v, l)
        if visited[w] == -1:
            p[w] = v
            bridges_aux(w)
            low[v] = min(low[v], low[w])

            # Verificar si es un puente
            if low[w] > visited[v]:
                bridges_set.add((v, w))
                bridges_set.add((w, v))
        elif w != p[v]:
            low[v] = min(low[v], visited[w])

def dfs_size(v, visited, exclude):
    visited[v] = True
    size = 1
    for w, _ in G[v]:
        if not visited[w] and (v, w) != exclude and (w, v) != exclude:
            size += dfs_size(w, visited, exclude)
    return size

def dfs_connected(v, visited):
    """Función DFS para marcar los nodos conectados."""
    visited[v] = True
    for w, _ in G[v]:
        if not visited[w]:
            dfs_connected(w, visited)            

def calculate_k():
    """Calcula el valor de k para cada puente, ignorando nodos desconectados."""
    global component_size, n
    component_size = {}
    # Primero, marcamos todos los nodos conectados
    visited = [False for _ in range(n+1)]
    dfs_connected(1, visited)  # Suponemos que el nodo 1 está conectado, y buscamos los alcanzables
    # Calculamos k solo para los nodos conectados
    for v, w in bridges_set:
        if (w, v) not in component_size:  # aun no calculamos el tamaño para este puente
            # Ignoramos los nodos desconectados, solo si estan conectados 
            if visited[v] or visited[w]:
                # Si ambos nodos están conectados, calculamos el tamaño de la componente
                visited_dfs = [False for _ in range(n+1)]
                # Tamaño de la componente que contiene `v`
                size_v = dfs_size(v, visited_dfs, (v, w))
                # Tamaño de la componente que contiene `w`
                size_w = n - size_v

                k = size_v * size_w
                component_size[(v, w)] = k

def can_distribute(texas, bridges, k_values, limit):
    """ Verifica si es posible distribuir los costos de los puentes bajo el límite dado. """
    taxes = texas[:] # Hacer una copia para no afectar a la lista original en las asignaciones 
    
    # Ordenar las aristas por k en orden descendente
    sorted_edges = sorted(k_values.items(), key=lambda item: item[1], reverse=True)
    # Es necesario procesar primero las aristas que tienen un mayor k Para asi asegurarse de
    # Hacer las asignaciones mas optimas posibles
    for (u, v), k in sorted_edges:
        l = bridges[(u, v)]  # Longitud de la carretera
        cost = l * k
        # Verifica si podemos asignar el costo a una de las dos ciudades sin exceder el límite
        print(f"u {u} to v {v}")
        print(f"taxes[u - 1] {taxes[u - 1]} + cost {cost}")
        print(f"taxes[v - 1] {taxes[v - 1]} + cost {cost}")
        if taxes[u - 1] + cost <= limit: # Restanmos uno porque taxes esta indexada desde 0
            taxes[u - 1] += cost
        elif taxes[v - 1] + cost <= limit:
            taxes[v - 1] += cost
        else:
            print(f"Cannot distribute: u={u}, v={v}, cost={cost} L{l} X K{k}, limit={limit}")
            return False  # No se puede distribuir sin superar el límite
    return True

def find_minimum_tax(texas, bridges, k_values):
    low, high = max(texas), sum(texas) + sum(k * l for (u, v), l in bridges.items() for _, k in k_values.items())
    result = high
    print(f"Initial low={low}, high={high}")
    while low <= high:
        mid = low + (high - low) // 2
        print(f"Trying mid={mid}")
        if can_distribute(texas, bridges, k_values, mid):
            result = mid
            high = mid - 1  # Buscamos límites más bajos
            print(f"Can distribute: new high={high}")
        else:
            low = mid + 1  # Incrementamos el límite
            print(f"Cannot distribute: new low={low}")
    print(f"Final result={result}")
    return result

def main():
    global G, n, visited, low, p, t, bridges_set
    line = stdin.readline()
    case_num = 1
    while line != "":
        n ,m = map(int, line.split())
        G = [[] for _ in range(n+1)]
        texas = list(map(int, stdin.readline().split()))
        bridges = {}
        
        for _ in range(m):
            u, v, l = map(int, stdin.readline().split())
            G[u].append((v, l))
            G[v].append((u, l))
            bridges[(u, v)] = l
            bridges[(v, u)] = l

        visited, low, p = [-1 for _ in range(n+1)], [-1 for _ in range(n+1)], [-1 for _ in range(n+1)]
        bridges_set, t = set(), 0
        bridges_tarjan()
        calculate_k()
        print(component_size)
        result = find_minimum_tax(texas, bridges, component_size)
        print(f"Case #{case_num}: The highest tax that must be paid to Emperor Zlatan is {result}.")
        print()
        stdin.readline()  # Línea vacía
        case_num += 1
        line = stdin.readline()

main()