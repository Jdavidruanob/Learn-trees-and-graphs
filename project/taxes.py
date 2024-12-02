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
        w = pair[0] #  v en (v, l)
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
    visited[v] = True
    for w, _ in G[v]:
        if not visited[w]:
            dfs_connected(w, visited)            

def calculate_k():
    global component_size
    component_size = {}
    for v, w in bridges_set:
        if (w, v) not in component_size:  
                visited_dfs = [False for _ in range(n+1)]
                size_v = dfs_size(v, visited_dfs, (v, w))
                size_w = dfs_size(w, visited_dfs, (v, w))
                k = size_v * size_w
                component_size[(v, w)] = k

def assign(cities, bridges, k_values, limit):
    ans = True
    cities_aux = cities[:]
    sorted_edges = sorted(k_values.items(), key=lambda item: item[1], reverse=True)
    for (u, v), k in sorted_edges:
        l = bridges[(u, v)]  
        cost = l * k
        if cities_aux[u - 1] + cost <= limit:
            cities_aux[u - 1] += cost
        elif cities_aux[v - 1] + cost <= limit:
            cities_aux[v - 1] += cost
        else:
            ans = False
    return ans

def binary_search(texas, bridges, k_values):
    low, high = max(texas),sum(texas) 

    total_bridge_cost = 0
    for (u, v), l in bridges.items():
        for _, k in k_values.items():
            total_bridge_cost += k * l
    high += total_bridge_cost

    ans = high
    while low <= high:
        mid = low + (high - low) // 2
        if assign(texas, bridges, k_values, mid):
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1  
    return ans

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
        ans = binary_search(texas, bridges, component_size)
        print(f"Case #{case_num}: The highest tax that must be paid to Emperor Zlatan is {ans}.")
        print()
        stdin.readline()  # Línea vacía
        case_num += 1
        line = stdin.readline()

main()