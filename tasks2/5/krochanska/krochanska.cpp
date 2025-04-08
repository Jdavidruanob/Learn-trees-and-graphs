/*
    Jose David Ruano Burbano 8982982
    Tarea 5 - Krochanska
    Arboles y grafos 2025-1

    Análisis de Complejidad:
    Sea n el número total de estaciones, m el número de aristas del grafo y k el número de estaciones importantes (k ≤ 100).
    - Identificación de estaciones importantes: O(n)
    - Para cada estación importante, se ejecuta Dijkstra:
        * Cada ejecución de Dijkstra: O(m log n)
        * Se repite k veces: O(k * m log n)

    En total, la complejidad seria algo como:
        O(n + k * m log n)
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <set>
#include <unordered_map>

using namespace std;

// Constantes
const int INF = INT_MAX;

// Variables globales
vector<vector<pair<int, int>>> graph;
vector<int> dist;

// Dijkstra estándar (uno a todos)
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

        if (dist[u] == du) {
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
    int t;
    cin >> t;

    while (t--) {
        int n, s, u, v;
        cin >> n >> s;
        graph.clear();
        graph.assign(n + 1, vector<pair<int, int>>());
        vector<int> stationLineCount(n + 1, 0);
        vector<vector<int>> lines(s);
        unordered_map<int, set<int>> lineMap;

        for (int i = 0; i < s; i++) {
            int station;
            while (cin >> station && station != 0) {
                lines[i].push_back(station);
                lineMap[station].insert(i);
            }
        }

        for (int i = 0; i < lines.size(); i++) {
            for (int j = 1; j < lines[i].size(); j++) {
                u = lines[i][j - 1];
                v = lines[i][j];
                graph[u].push_back({v, 2});
                graph[v].push_back({u, 2});
            }
        }
        vector<int> importantStations;
        for (int i = 1; i <= n; i++) {
            if (lineMap[i].size() > 1) {
                importantStations.push_back(i);
            }
        }

        int station, ans = -1;
        double bestAvg = INF;

        for (int i = 0; i < importantStations.size(); i++) {
            station = importantStations[i];
            vector<int> d = dijkstra(graph, station);
            long long sum = 0;
            for (int j = 0; j < importantStations.size(); j++) {
                int other = importantStations[j];
                if (station != other) {
                    sum += d[other];
                }
            }
            double avg = (double)sum / (importantStations.size() - 1);
            if (avg < bestAvg || (avg == bestAvg && station < ans)) {
                bestAvg = avg;
                ans = station;
            }
        }
        cout << "Krochanska is in: " << ans << '\n';
    }

    return 0;
}
