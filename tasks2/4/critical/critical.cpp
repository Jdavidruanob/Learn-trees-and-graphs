#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<vector<int>> G;
vector<int> capacity;
vector<bool> visited;
vector<int> low, disc, parent;
set<int> articulationSet;
int t, n, m;

void articulationAux(int v) {
    t++;
    visited[v] = true;
    low[v] = disc[v] = t;
    int children = 0;

    for (int w : G[v]) {
        if (!visited[w]) {
            parent[w] = v;
            children++;
            articulationAux(w);
            low[v] = min(low[v], low[w]);

            if (parent[v] == -1 && children > 1)
                articulationSet.insert(v);
            if (parent[v] != -1 && low[w] >= disc[v])
                articulationSet.insert(v);
        } else if (w != parent[v]) {
            low[v] = min(low[v], disc[w]);
        }
    }
}

void findArticulationPoints() {
    visited.assign(n, false);
    low.assign(n, -1);
    disc.assign(n, -1);
    parent.assign(n, -1);
    articulationSet.clear();
    t = 0;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            articulationAux(i);
        }
    }
}

int countComponents(int exclude) {
    vector<bool> tempVisited(n, false);
    int components = 0;

    for (int i = 0; i < n; i++) {
        if (i == exclude || tempVisited[i]) continue;
        components++;
        vector<int> stack = {i};
        while (!stack.empty()) {
            int v = stack.back(); stack.pop_back();
            tempVisited[v] = true;
            for (int w : G[v]) {
                if (!tempVisited[w] && w != exclude) {
                    stack.push_back(w);
                }
            }
        }
    }
    return components;
}

int main() {
    while (cin >> n >> m) {
        G.assign(n, vector<int>());
        capacity.resize(n);
        
        for (int i = 0; i < n; i++) {
            cin >> capacity[i];
        }
        
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            G[u].push_back(v);
            G[v].push_back(u);
        }
        
        findArticulationPoints();
        if (articulationSet.empty()) {
            cout << "-1" << endl;
            continue;
        }
        
        int maxDisconnected = 0, bestStation = -1;
        for (int v : articulationSet) {
            int disconnected = countComponents(v) - 1;
            if (disconnected > maxDisconnected || 
                (disconnected == maxDisconnected && capacity[v] > capacity[bestStation]) || 
                (disconnected == maxDisconnected && capacity[v] == capacity[bestStation] && v < bestStation)) {
                maxDisconnected = disconnected;
                bestStation = v;
            }
        }
        
        cout << bestStation << " " << maxDisconnected << endl;
    }
    return 0;
}
