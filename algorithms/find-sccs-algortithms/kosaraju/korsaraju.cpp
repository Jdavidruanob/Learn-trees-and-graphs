#include <vector>
#include <list>
using namespace std;

vector<vector<int>> graph, graphT;
vector<bool> visited;
vector<int> sccInd;
list<int> order;
int num;

void dfs1(int u);
void dfs2(int u);
int kosaraju(int n);

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
