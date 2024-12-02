/*  Jose David Ruano Burbano
    8982982
    Arboles y grafos
    Tarea 4 - Water
    Analisis complejidad: 

    El algoritmo implementado tiene una complejidad temporal de O(N + M),
    donde N es el numero de nodos y M es el numero de aristas. 
    Esto se debe a que se hizo uso del algoritmo de Gabow para encontrar 
    componentes fuertemente conexos (SCC) y al final en todas las partes del codigo
    la complejidad mas grande es la de O(N + M) .
    
    */

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

void gabowAux(int v, vector<vector<int>>& graph, vector<int>& vis, vector<int>& sccInd, stack<int>& pilaS, stack<int>& pilaP, int& t, int& numSCC, vector<vector<int>>& sccs) {
    
    vis[v] = ++t; 
    pilaS.push(v); 
    pilaP.push(v); 

    
    for (int i = 0; i < graph[v].size(); i++) {
        int w = graph[v][i];
        if (vis[w] == -1) {
            gabowAux(w, graph, vis, sccInd, pilaS, pilaP, t, numSCC, sccs);
        } else if (sccInd[w] == -1) {
            while (vis[pilaP.top()] > vis[w]) {
                pilaP.pop();
            }
        }
    }

    if (v == pilaP.top()) {
        vector<int> scc;
        numSCC++;
        while (pilaS.top() != v) {
            scc.push_back(pilaS.top());
            sccInd[pilaS.top()] = numSCC - 1;
            pilaS.pop();
        }
        scc.push_back(pilaS.top());
        sccInd[pilaS.top()] = numSCC - 1;
        pilaS.pop();
        pilaP.pop();
        sccs.push_back(scc);
    }
}

void gabow(int n, vector<vector<int>>& graph, vector<vector<int>>& sccs) {
    /* Algoritmo de Gabow para encontrar las componentes fuertemente conexas de un grafo. */
    vector<int> vis(n + 1, -1);
    vector<int> sccInd(n + 1, -1);
    stack<int> pilaS, pilaP;
    int t = 0, numSCC = 0;

    for (int i = 0; i <= n; i++) {
        if (vis[i] == -1) {
            gabowAux(i, graph, vis, sccInd, pilaS, pilaP, t, numSCC, sccs);
        }
    }
}

int main() {
    int n, m, a, b;
    while (cin >> n >> m) {
        // leer grafo
        vector<vector<int>> graph(n + 1);
        for (int i = 0; i < m; i++) {
            cin >> a >> b;
            graph[a].push_back(b);
        }

        // Obtener scc usando Gabow
        vector<vector<int>> sccs;
        gabow(n, graph, sccs);

        // Asignamos un id de scc a cada nodo del grafo original
        vector<int> sccId(n + 1, -1); 
        for (int i = 0; i < sccs.size(); i++) {
            for (int j = 0; j < sccs[i].size(); j++) {
                int node = sccs[i][j];
                sccId[node] = i;
            }
        }

        // Construimos grafo de sccs y calculamos le grado de incidencia
        vector<vector<int>> sccGraph(sccs.size());
        vector<int> inDegree(sccs.size(), 0);

        for (int u = 0; u <= n; u++) {
            for (int j = 0; j < graph[u].size(); j++) {
                int v = graph[u][j];
                if (sccId[u] != sccId[v]) {
                    sccGraph[sccId[u]].push_back(sccId[v]);
                    inDegree[sccId[v]]++;
                }
            }
        }
        // Contamos cuantos sccs tiene grado de incidencia 0
        int newPipelines = 0;
        for (int i = 0; i < sccs.size(); i++) {
            if (inDegree[i] == 0 && i != sccId[0]) {
                newPipelines++;
            }
        }
        // Imprimimos la salida
        cout << newPipelines << endl;
    }

    return 0;
}