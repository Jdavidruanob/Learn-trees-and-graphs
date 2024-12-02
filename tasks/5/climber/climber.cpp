/* 
Jose David Ruano
8982982
Arboles y grafos

Analisis de la complejidad: 
La complejidad del algoritmo para ssspDag es O(N + F), donde N es el número de puntos de referencia y F es el número de amigos.

El algoritmo de orden topologico tiene una complejidad de O(N), ya que recorre todos los nodos y aristas.

El cálculo de las distancias mínimas utilizando una cola de prioridad tiene una complejidad de O(N log N).

El cálculo de la energía total requerida para visitar a todos los amigos tiene una complejidad de O(F).
Por lo tanto
la complejidad total del algoritmo es O(N log N + F), siendo esta la parte predominante.
  
*/
#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

const double INF = numeric_limits<double>::infinity();
vector<vector<pair<int,int>>> G, GInvert;
vector<double> dist;
int energy = 0;

vector<int> topoSort() {
    queue<int> q;
    vector<int> topo, inc(G.size(), 0);
    for (int u = 0; u < G.size(); ++u) {
        for (const pair<int,int>& edge : G[u]) {
            int v = edge.first;
            inc[v] += 1;
        }
    }
    for (int u = 0; u < G.size(); ++u) {
        if (inc[u] == 0) q.push(u);
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topo.push_back(u);
        for (const pair<int,int> & edge : G[u]) {
            int v = edge.first;
            inc[v] -= 1;
            if (inc[v] == 0) q.push(v);
        }
    }
    return topo;
}

pair<vector<double>, vector<int>> ssspDAG(int s) {
    vector<double> dist(G.size(), INF);
    vector<int> pred(G.size(), -1), topo = topoSort();
    dist[s] = 0;
    for (int u : topo) {
        for (const pair<int,int> & v_duv : G[u]) {
            int v = v_duv.first;
            double duv = v_duv.second;
            if (dist[u] + duv < dist[v]) {
                dist[v] = dist[u] + duv;
                pred[v] = u;
            }
        }
    }
    return make_pair(dist, pred);
}

void dfs(int u, vector<bool>& vis) {
    for (int i = 0; i < GInvert[u].size(); i++) {
        int v = GInvert[u][i].first;
        int weight = GInvert[u][i].second;
        if (!vis[u]) {
            vis[u] = true;
            energy += weight;
            dfs(v, vis); 
        }
    }
}

int main() {
    int n, f, a, b, c, li; 
    while (cin >> n >> f) {
        G.clear();
        G.resize(n + 1);
        GInvert.clear();
        GInvert.resize(n+1);
        vector<int> friends(f);
        vector<bool> vis (n + 1, false);
        priority_queue<pair<int,int>> q, q_copy;

        for (int i = 0; i < n - 1; i++) {
            cin >> a >> b >> c;
            G[a].push_back(make_pair(b, c));
            GInvert[b].push_back(make_pair(a, c));
        }
        for (int i = 0; i < f; i++) {
            cin >> li;
            friends[i] = li;  
        }
        dist = ssspDAG(1).first;
        for(int i = 0; i< f; ++i){
            q.push( make_pair(dist[friends[i]] , friends[i])); 
        }
        q_copy = q;
        energy = 0;
        int node = q_copy.top().second;
        q_copy.pop();
        dfs(node, vis);
        energy = 0;
        while (!q_copy.empty()) {
            node = q_copy.top().second;
            q_copy.pop();
            dfs(node, vis);
        }
        cout << energy << endl;
    }
    return 0;
}