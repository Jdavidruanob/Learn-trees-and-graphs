/* 
Jose David Ruano Burbano 8982982
Tarea 3 - coaches
Arboles y grafos 2025-1

Analisis complejidad:
Siendo N el número de entrenadores, y M el 
número de relaciones de entrenamiento entre ellos:
- Construcción del grafo: O(N + M)
- Ordenamiento topologico (BFS): O(N + M)
- Ordenamiento por generacion: O(N log N)
En total, la complejidad es O(N log N + M), Asi la complejidad total 
es O(N log N) siendo el termino dominante.

*/

#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Coach {
    string name;
    int birth_year;
    int trained_count;
    
    Coach() : name(""), birth_year(0), trained_count(0) {}
    Coach(string n, int y) : name(n), birth_year(y), trained_count(0) {}
    
    bool operator<(const Coach &other) const {
        bool ans;
        if (trained_count != other.trained_count) 
            ans = trained_count > other.trained_count;
        else{
            if (birth_year != other.birth_year)
                ans = birth_year < other.birth_year;
            else{
                ans = name < other.name;
            }
        }
        return ans;
    }
};

void solve() {
    int N, M;
    cin >> N >> M;
    
    unordered_map<string, Coach> coaches;
    unordered_map<string, vector<string>> G;
    unordered_map<string, int> in_degree;
    
    for (int i = 0; i < N; i++) {
        string name;
        int year;
        cin >> name >> year;
        coaches[name] = Coach(name, year);
        G[name] = vector<string>();
        in_degree[name] = 0;
    }
    
    for (int i = 0; i < M; i++) {
        string coach, player;
        cin >> coach >> player;
        G[coach].push_back(player);
        coaches[coach].trained_count++;
        in_degree[player]++;
    }
    
    queue<pair<string, int>> q;
    unordered_map<int, vector<Coach>> generations;
    int max_generation = 0;
    
    for (unordered_map<string, int>::iterator it = in_degree.begin(); it != in_degree.end(); ++it) {
        string name = it->first;
        int deg = it->second;
        if (deg == 0) {
            q.push(make_pair(name, 0));
            generations[0].push_back(coaches[name]);
        }
    }
    
    while (!q.empty()) {
        pair<string, int> current = q.front();
        q.pop();
        string coach_name = current.first;
        int gen = current.second;
        max_generation = max(max_generation, gen);
        
        for (int i = 0; i < G[coach_name].size(); i++) {
            string player = G[coach_name][i];
            in_degree[player]--;
            if (in_degree[player] == 0) {
                q.push(make_pair(player, gen + 1));
                generations[gen + 1].push_back(coaches[player]);
            }
        }
    }
    
    for (int g = 0; g < max_generation; g++) {
        sort(generations[g].begin(), generations[g].end());
        if (!generations[g].empty()) {
            cout << "Generation " << g << ": " << generations[g][0].name << endl;
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Scenario #" << i << ":" << endl;
        solve();
        if (i < T) cout << endl;  // Separar casos con línea en blanco
    }
    
    return 0;
}
