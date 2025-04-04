def tarjan_scc_aux(u, graph):
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



    
    
