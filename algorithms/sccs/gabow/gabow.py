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
            scc.append(pila_s.pop())
            scc_ind[scc[-1]] = num_scc[0] - 1
        scc.append(pila_s.pop())
        scc_ind[scc[-1]] = num_scc[0] - 1
        pila_p.pop()
        sccs.append(scc)

def gabow(n, graph):
    """ Algoritmo de Gabow para encontrar las componentes fuertemente conexas. """
    
    vis = [-1] * (n + 1)
    scc_ind = [-1] * (n + 1)
    pila_s = []
    pila_p = []
    t = [0]  # Contador de tiempo como lista para que sea mutable en la recursión
    num_scc = [0]  # Contador de SCCs
    
    sccs = []
    for i in range(n + 1):
        if vis[i] == -1:
            gabow_aux(i, graph, vis, scc_ind, pila_s, pila_p, t, num_scc, sccs)

    return sccs
