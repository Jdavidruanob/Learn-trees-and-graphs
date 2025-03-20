/* 
    Jose David Ruano Burbano 8982982
    Tarea 4 - critical
    Arboles y grafos 2025-1

    Analisis de complejidad: 
    Siendo n el número de estaciones y m el número de conexiones entre estaciones:

    - Construcción del grafo: O(n + m)
    - Búsqueda de puntos de articulación (Tarjan): O(n + m)
    - Calculo de estaciones desconectadas (DFS por cada punto de articulación): O(n + m) en promedio
    - Ordenamiento de estaciones criticas: O(n log n)

    En total, la complejidad esperada es O(n log n + m), aunque en el peor caso podria llegar a O(n (n + m)).
*/

#include <vector> 
#include <iostream>
#include <algorithm>
using namespace std;

// global vars 
vector<bool> ap, visited;
vector<vector<int>> graph;
vector<int> low, disc, p, capacity;
int t;

// structure
struct CriticalStation{
    int id;
    int disconnected;
    int capacity;

    bool operator<(const CriticalStation & c) const{
        bool ans;
        if (disconnected != c.disconnected){
            ans = disconnected > c.disconnected;
        } else {
            if (capacity != c.capacity){
                ans = capacity > c.capacity;
            } else {
                if (id != c.id){
                    ans = id < c.id;
                }
            }
        }
        return ans;
    }
};

// fuctions to use
void findArtPoints(int n);
void artPointsAux(int v);
int dfsCount(int v, int n);
vector<CriticalStation> find_critical_stations(int n);

int main(){
    int n, m, u, v;
    while(cin >> n >> m){
        graph.clear();
        ap.clear();
        visited.clear();
        low.clear();
        disc.clear();
        p.clear();
        capacity.clear();

        graph.assign(n, vector<int> ());
        capacity.resize(n);
        for (int i = 0; i < n; i++) 
            cin >> capacity[i];
        for (int i = 0; i < m; i++){
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }  

        findArtPoints(n);
        vector<CriticalStation> ans = find_critical_stations(n);
        if (ans.empty()) {
            cout << "-1" << endl;
        }
        else{
            sort(ans.begin(), ans.end());
            cout << ans[0].id << " " << ans[0].disconnected << endl;
        }
    
    }
    return 0;
}
/*
    Use tarjan and hope algorithm to find
    articule points
*/
void findArtPoints(int n) {
    disc.assign(n, -1);
    low.assign(n, -1);
    p.assign(n, -1);
    visited.assign(n, false);
    ap.assign(n, false);
    t = 0;
    
    for(int i = 0; i < n; i++) {
        if (!visited[i])
            artPointsAux(i);
    }
}
void artPointsAux(int v) {
    int childs = 0;
    visited[v] = true;
    disc[v] = t; 
    low[v] = t;
    t++;          

    for (int w : graph[v]) {
        if (!visited[w]) {
            childs++;
            p[w] = v;
            artPointsAux(w);
            low[v] = min(low[v], low[w]);

            // Caso raiz
            if (p[v] == -1 && childs > 1)
                ap[v] = true;
            // Caso no raiz
            if (p[v] != -1 && low[w] >= disc[v])
                ap[v] = true;
        }
        else if (w != p[v]) {
            low[v] = min(low[v], disc[w]);  // Usar disc[w] en lugar de low[w]
        }
    }
}

/*
    DFS to count nodes that disconnected whithout 
    articulation point
*/
int dfsCount(int v, int n){
    visited[v] = true;
    int count = 1;
    for (int w : graph[v]){
        if(!visited[w])
            count += dfsCount(w, n);
    }
    return count;
}

/* 
    Function to find all critical stations
*/
vector<CriticalStation> find_critical_stations(int n){
    vector<CriticalStation> ans;
    for(int i = 0; i < n; i++){
        if(ap[i]){
            visited.assign(n, false);
            int count = dfsCount(i, n) - 1;
            ans.push_back({i, count, capacity[i]});
        }
    }
    return ans;
}
