/* 
    Jose David Ruano Burbano 8982982
    Tarea 4 - impossible
    Arboles y grafos 2025-1

    Análisis de Complejidad:
    Siendo n los grupos de investigación y m las relaciones entre grupos:

    - Construcción del grafo y su transpuesto: O(n + m)
    - Algoritmo de Kosaraju:
        * Primer DFS (ordenamiento topológico): O(n + m)
        * Segundo DFS (encontrar SCCs): O(n + m)
    - Verificación de número de SCCs: O(n)

    En total, la complejidad es O(n + m).
*/


#include <iostream>
#include <vector>
#include <list>

using namespace std;

// Variables globales
vector<vector<int>> graph, graphT;
vector<bool> visited;
vector<int> sccInd;
list<int> order;
int num;

// functions
void dfs1(int u);
void dfs2(int u);
int kosaraju(int n);

int main() {
    int n, m;
    while (cin >> n >> m) {
        graph.assign(n + 1, vector<int>());
        graphT.assign(n + 1, vector<int>());

        for (int i = 0; i < m; i++) {
            int k;
            cin >> k;
            
            if (k == 1) {
                // simple
                int from, to;
                cin >> from >> to;
                graph[from].push_back(to);
                graphT[to].push_back(from);
            } else {
                //  complejo
                vector<int> nodes(k);
                for (int j = 0; j < k; j++) {
                    cin >> nodes[j];
                }
                
                // Conectar todos los nodos del grupo
                if (k >= 2) {
                    int rep = nodes[0];
                    for (int j = 1; j < k; j++) {
                        int node = nodes[j];
                        graph[rep].push_back(node);
                        graph[node].push_back(rep);
                        graphT[rep].push_back(node);
                        graphT[node].push_back(rep);
                    }
                }
            }
        }
        if (kosaraju(n) == 1) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    return 0;
}

/*
    Kosaraju para encontrar componentes fuertemente conexos
*/
int kosaraju(int n) {
    visited.assign(n + 1, false);
    order.clear();
    num = 0;
    
    for(int i = 1; i <= n; i++) {
        if(!visited[i]) {
            dfs1(i);
        }
    }
    visited.assign(n + 1, false);
    sccInd.assign(n + 1, -1);
    for(int u : order) {
        if(!visited[u]) {
            dfs2(u);
            num++;
        }
    }
    return num;
}

/*
    dfs 1 para ordenar nodos según orden de finalización
*/
void dfs1(int u) {
    visited[u] = true;
    for(int v : graph[u]) {
        if(!visited[v]) {
            dfs1(v);
        }
    }
    order.push_front(u);
}

/*
    dfs 2 para asignar índice de componente fuertemente conexo
*/
void dfs2(int u) {
    sccInd[u] = num;
    visited[u] = true;
    for(int v : graphT[u]) {
        if(!visited[v]) {
            dfs2(v);
        }
    }
}



