/* 
    Jose David Ruano Burbano 8982982
    Tarea 5 - Cards
    Arboles y grafos 2025-1

    Analisis de Complejidad:
    Siendo p el numero de paradas y q el numero de lineas de bus:

    - Ejecucion de Dijkstra desde CCS (parada 1):
        * En el grafo original (ida): O((p + q) * log p)
        * En el grafo transpuesto (regreso): O((p + q) * log p)

    - Calculo de suma de distancias: O(p)
    En total, la complejidad es O((p + q) * log p).
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// const
const int INF = INT_MAX;

// global vars
vector<vector<pair<int, int>>> graph;     
vector<vector<pair<int, int>>> graphT;   
vector<int> dist;

// Dijkstra (one to all)
vector<int> dijkstra(vector<vector<pair<int, int>>>& G, int s) {
    int n = G.size();
    dist.assign(n, INF);
    dist[s] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, s});

    while (!pq.empty()) {
        int du = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (dist[u] == du){
            for (pair<int, int> edge : G[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (du + weight < dist[v]) {
                    dist[v] = du + weight;
                    pq.push({dist[v], v});
                }
            }
        }
    }

    return dist;
}

int main() {
    int n; 
    cin >> n;

    while (n--) {
        int p, q; 
        cin >> p >> q;

        graph.clear(); graphT.clear();
        graph.assign(p + 1, vector<pair<int, int>>());
        graphT.assign(p + 1, vector<pair<int, int>>());

        for (int i = 0; i < q; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            graph[u].push_back({v, w});
            graphT[v].push_back({u, w}); 
        }
        vector<int> distGo = dijkstra(graph, 1);
        vector<int> distBack = dijkstra(graphT, 1);

        long long ans = 0;
        for (int i = 2; i <= p; i++) {
            ans += distGo[i];
            ans += distBack[i];
        }
        cout << ans << '\n';
    }
    return 0;
}
