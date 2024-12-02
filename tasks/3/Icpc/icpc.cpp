/* Jose David Ruano Burbano 8982982
Tarea 3 - Icpc
Arboles y grafos 2024-2
Universidad Pontificia Javeniana cali */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int count(vector<int>& E, vector<vector<int>>& G, vector<int>& in_degree) {
    // Funcion usando Bfs de dos colas

    queue<int> qKarina, qIsaringa;
    int count = 0; 
    // Agregar a las colas los nodos que tienen grado de incidencia 0
    for (int i = 0; i < G.size(); ++i) {
        if (in_degree[i] == 0) {
            if (E[i] == 0) qKarina.push(i); 
            else {
                qIsaringa.push(i); 
            }
        }
    }

    // mientras hayan problemas para resolver
    while (!qKarina.empty() || !qIsaringa.empty()) {

        // Procesar los problemas de Karina
        while (!qKarina.empty()) {
            int u = qKarina.front();
            qKarina.pop();
            for (int j = 0; j < G[u].size(); ++j) {
                int v = G[u][j]; // nodo a visitar
                in_degree[v]--; // disminuir el grado de incidencia
                if (in_degree[v] == 0) { // si esta disponible
                    if (E[v] == 0) qKarina.push(v); // si es de programacion dinamica
                    else {
                        qIsaringa.push(v); // si es un problema matemático
                    }
                }
            }
        }

        // si hay para isaringa
        if (!qIsaringa.empty()) {
            count++; // contamos el llamado a isaringa

            // Procesar los problemas de Isaringa
            while (!qIsaringa.empty()) {
                int u = qIsaringa.front();
                qIsaringa.pop();
                for (int j = 0; j < G[u].size(); ++j) {
                    int v = G[u][j];
                    in_degree[v]--;
                    if (in_degree[v] == 0) {
                        if (E[v] == 0) qKarina.push(v); 
                        else {
                            qIsaringa.push(v); 
                        }
                    }
                }
            }
        }
    }

    return count; 
}

int main() {
    int c;
    cin >> c;

    while (c--) {
        int n, m, ans;
        // lerr la entrada 
        cin >> n >> m;
        vector<vector<int>> G(n); // grafo
        vector<int> in_degree(n, 0); // grado de incidencia 
        vector<int> E(n); // tipo de problema

        // leer los problemas
        for (int i = 0; i < n; ++i) {
            cin >> E[i];
        }

        // crear el grafo y obtener el grado de incidencia
        for (int i = 0; i < m; ++i) {
            int p1, p2;
            cin >> p1 >> p2;
            G[p2].push_back(p1); 
            in_degree[p1]++; 
        }

        ans = count(E, G, in_degree);
        // imprimir salida
        cout << ans << endl;
    }

    return 0;
}