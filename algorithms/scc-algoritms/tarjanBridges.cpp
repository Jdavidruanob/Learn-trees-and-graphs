#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> G;
vector<bool> visited;
vector<int> low, p;
set<pair<int, int>> bridgesSet;
int t, n, m;

void bridgesAux(int v) {
    t++;
    visited[v] = true;
    low[v] = t;

    for (int w : G[v]) {
        if (!visited[w]) {
            p[w] = v;
            bridgesAux(w);
            low[v] = min(low[v], low[w]);

            // Verificar si es un puente
            if (low[w] > low[v]) {
                bridgesSet.insert({v, w});
            }
        } else if (w != p[v]) {
            low[v] = min(low[v], low[w]);
        }
    }
}

void bridgesTarjan() {
    for (int i = 0; i < n; ++i) {
        low[i] = visited[i] = p[i] = -1;
    }

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            bridgesAux(i);
        }
    }
}

int main() {
    cin >> n >> m;
    G.assign(n, vector<int>());
    visited.assign(n, false);
    low.assign(n, -1);
    p.assign(n, -1);
    t = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    bridgesTarjan();

    if (bridgesSet.empty()) {
        cout << "El grafo no tiene puentes" << endl;
    } else {
        cout << "Total puentes: " << bridgesSet.size() << endl;
        for (const auto &bridge : bridgesSet) {
            cout << bridge.first << " " << bridge.second << endl;
        }
    }

    return 0;
}