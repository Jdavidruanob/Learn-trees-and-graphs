#include <vector> 
#include <iostream>
#include <algorithm>
using namespace std;

// global vars 
vector<bool> ap, visited;
vector<vector<int>> graph;
vector<int> low, disc, p, capacity;
int t;

// fuctions to use
void tarjanAP(int n);
void tarjanAPaux(int v);

/*
    Use tarjan and hope algorithm to find
    articule points
*/
void tarjanAP(int n) {
    disc.assign(n, -1);
    low.assign(n, -1);
    p.assign(n, -1);
    visited.assign(n, false);
    ap.assign(n, false);
    t = 0;
    
    for(int i = 0; i < n; i++) {
        if (!visited[i])
            tarjanAPaux(i);
    }
}
void tarjanAPaux(int v) {
    int childs = 0;
    visited[v] = true;
    disc[v] = t; 
    low[v] = t;
    t++;          

    for (int w : graph[v]) {
        if (!visited[w]) {
            childs++;
            p[w] = v;
            tarjanAPaux(w);
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