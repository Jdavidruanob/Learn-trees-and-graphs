#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Constantes
const int INF = INT_MAX;
const int MAXN = 100005;

// Variables globales
vector<vector<pair<int, int>>> graph;       // Grafo original
vector<vector<pair<int, int>>> rev_graph;   // Grafo transpuesto
vector<int> dist;

// Algoritmo de Dijkstra (uno-a-todos)
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

        if (dist[u] < du) continue;

        for (pair<int, int> edge : G[u]) {
            int v = edge.first;
            int weight = edge.second;
            if (du + weight < dist[v]) {
                dist[v] = du + weight;
                pq.push({dist[v], v});
            }
        }
        
    }

    return dist;
}

int main() {
    int N; // Número de casos
    cin >> N;

    while (N--) {
        int P, Q; // P: número de paradas, Q: número de líneas
        cin >> P >> Q;

        // Inicializar grafos
        graph.clear(); rev_graph.clear();
        graph.assign(P + 1, vector<pair<int, int>>());
        rev_graph.assign(P + 1, vector<pair<int, int>>());

        for (int i = 0; i < Q; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            graph[u].push_back({v, w});
            rev_graph[v].push_back({u, w}); // Reversa para regreso
        }

        // Dijkstra desde CCS (nodo 1) en ambos grafos
        vector<int> dist_go = dijkstra(graph, 1);
        vector<int> dist_back = dijkstra(rev_graph, 1);

        // Calcular el total del costo diario
        long long total_cost = 0;
        for (int i = 2; i <= P; i++) {
            total_cost += dist_go[i];
            total_cost += dist_back[i];
        }

        cout << total_cost << '\n';
    }

    return 0;
}
