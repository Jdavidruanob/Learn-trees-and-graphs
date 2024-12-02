/* 
Jose David Ruano
8982982
Arboles y grafos

Analisis de la complejidad: 
La complejidad del algoritmo Bellman-Ford modificado es O(n * m), donde n es el número de sistemas estelares y m es el número de agujeros de gusano.
Esto se debe a que el bucle externo se ejecuta O(n) veces y el bucle interno que relaja las aristas se ejecuta O(m) veces.

La inicialización de vectores tiene una complejidad de O(n).

El DFS auxiliar que se ejecuta después de Bellman-Ford tiene una complejidad de O(n + m), ya que recorre todos los nodos y aristas.

Por lo tanto la complejidad total del algoritmo es O(n * m), siendo esta la parte predominante.
  
*/
#include <iostream>
#include <vector>
#include <limits>
using namespace std;
const int INF = numeric_limits<int>::max();
int n, m;
vector<int> dist, cycle, vis;
vector<vector<pair<int, int>>> G;

vector<int> bellmanFordDetCic() {
    dist.resize(n, 0);
    cycle.resize(n, 0);
    bool flag = true;
    for (int i = 0; i < n - 1 && flag; ++i) {
        flag = false;
        for (int u = 0; u < n; ++u) {
            for (const pair<int, int>& edge : G[u]) {
                int v = edge.second;   
                int weight = edge.first;
                if (dist[u] != INF && dist[v] > dist[u] + weight) {
                    dist[v] = dist[u] + weight;
                    flag = true;
                }
            }
        }
    }
    for (int u = 0; u < n; ++u) {
        for (const pair<int, int>& edge : G[u]) {
            int v = edge.second;
            int weight = edge.first;
            if (dist[u] != INF && dist[v] > dist[u] + weight) {
                cycle[u] = 1;
                cycle[v] = 1;
            }
        }
    }
    return cycle;
}

void dfsAux(int u) {
    vis[u] = 1;
    for (const pair<int, int>& edge : G[u]) {
        int v = edge.second;
        if (!vis[v]) {
            cycle[v] = 1;
            dfsAux(v);
        }
    }
}

void dfs() {
    vis.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        if (cycle[i] == 1) {
            dfsAux(i);
        }
    }
}

int main() {
    int t, x, y, z;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> m;
        G.clear();
        G.resize(n);
        dist.clear();
        cycle.clear();
        vis.clear();
        for (int i = 0; i < m; ++i) {
            cin >> x >> y >> z;
            G[y].push_back({z, x});
        }
        bellmanFordDetCic(); 
        dfs();
        bool flag = true;
        cout << "Case " << i << ":";
        for (int i = 0; i < n; ++i) {
            if (cycle[i] == 1) {
                cout << " " << i;
                flag = false;
            }
        }
        if (flag) {
            cout << " impossible";
        }
        cout << endl;
    }
    return 0;
}
