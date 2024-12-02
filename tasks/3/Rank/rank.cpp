/* Jose David Ruano Burbano 8982982
Tarea 3 - Rank 
Arboles y grafos 2024-2
Universidad Pontificia Javeniana cali */

#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs_mod_aux(int x, int y, vector<vector<char>>& matrix, vector<vector<bool>>& vis, char l) {
    int h = matrix.size();
    int w = matrix[0].size();
    queue<pair<int, int>> q; 
    
    q.push({x, y});
    vis[x][y] = true;

    while (!q.empty()) {
        // obtener el primer elemento de la cola
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        // marcarlos como visitados si son del mismo lenguaje l 
        for (int k = 0; k < 4; ++k) {
            int nx = cx + dx[k];
            int ny = cy + dy[k];

            if (nx >= 0 && nx < h && ny >= 0 && ny < w && !vis[nx][ny] && matrix[nx][ny] == l) {
                vis[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

map<char,int> bfs_mod(int h, int w, vector<vector<char>>& matrix, vector<vector<bool>>& vis, map<char,int>& lCount) {

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (!vis[i][j]) {
                    char l = matrix[i][j]; // lenguaje
                    bfs_mod_aux(i, j, matrix, vis, l);
                    lCount[l]++; // contar region del lenguaje l
                }
            }
        }
    return lCount;
}


bool compare(const pair<int, char>& a, const pair<int, char>& b) {
    // Funcion para pasarsela a sort y ordenar los lenguajes lexograficamente
    bool ans;
    if (a.first != b.first) {
        ans = a.first > b.first;
    } 
    else {
        ans = a.second < b.second;
    }
    return ans;
}

int main() {
    int t, k, h, w;
    cin >> t;

    while(k < t){ 
        
        cin >> h >> w;
        vector<vector<char>> matrix(h, vector<char>(w)); // matriz de caracteres
        map<char, int> lCount; // map para contar cuántas veces aparece cada lenguaje
        vector<vector<bool>> vis(h, vector<bool>(w, false)); // matriz de visitados


        // leer la matriz
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                cin >> matrix[i][j];
            }
        }

        lCount = bfs_mod(h, w, matrix, vis, lCount); 

        // ordenar los lenguajes lexicograficamente
        vector<pair<int, char>> sortedl; // vector para ordenar los lenguajes

        // pasar los lenguajes al vector para luego ordenarlos
        for (map<char, int>::iterator it = lCount.begin(); it != lCount.end(); ++it) {
            sortedl.push_back(make_pair(it->second, it->first));
        }
        sort(sortedl.begin(), sortedl.end(), compare);

        // imprimir salida
        cout << "World #" << k+1 << endl;
        for (int i = 0; i < sortedl.size(); ++i) {
            cout << sortedl[i].second << ": " << sortedl[i].first << endl;
        }
        k++;
    }
    return 0;
}