/* 
    Jose David Ruano Burbano 8982982
    Tarea 4 - dominos
    Arboles y grafos 2025-1

    Análisis de Complejidad:
    Siendo n el número de dominós y m el número de relaciones entre dominós:

    - Construcción del grafo y su transpuesto: O(n + m)
    - Algoritmo de Kosaraju:
        * Primer DFS (ordenamiento): O(n + m)
        * Segundo DFS (encontrar SCCs): O(n + m)
    - Cálculo de grados de entrada entre SCCs: O(m)
    - Conteo de SCCs sin incidencias: O(n)

    En total, la complejidad es O(n + m).
*/

#include <iostream>
#include <vector>
#include <list>

using namespace std;

// global vars
vector<vector<int>> graph, graphT;
vector<bool> visited;
vector<int> sccInd;
list<int> order;
int num;

// functions
void dfs1(int u);
void dfs2(int u);
int kosaraju(int n);

int main(){
    int t, n, m, x, y;
    cin >> t;
    for(int i = 0; i < t; i++){
        graph.clear();
        graphT.clear();
        cin >> n >> m;
        graph.assign(n+1, vector<int>());
        graphT.assign(n+1, vector<int>());
        
        for(int j = 0; j < m; j++){
            cin >> x >> y;
            graph[x].push_back(y);
            graphT[y].push_back(x);
        }
        
        int numSCC = kosaraju(n);
        vector<int> inDegree(numSCC, 0);
        
        for(int u = 1; u <= n; u++) {
            for(int v : graph[u]) {
                if(sccInd[u] != sccInd[v]) {
                    inDegree[sccInd[v]]++;
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < numSCC; i++) {
            if(inDegree[i] == 0) {
                ans++;
            }
        }
        cout << ans << endl;
    }
    return 0;
}

/*
    Kosaraju to find scc
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
    dfs 1 to order nodes in finalization order
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
    dfs2 to assign scc id
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
