#include <vector>
#include <stack>
#include <iostream>
#include <map>

using namespace std;

int n, numSCC, t;
map<char, vector<char>> adj;
map<char, int> visitado, low, padre;
vector<vector<pair<char, char>>> comps;
stack<pair<char, char>> pila;

void bcAux(char v){
    int numHijos = 0;
    visitado[v] = low[v] = ++t;
    cout << "\nEntra a bcAux(" << v << ")" << endl;
    cout << "visitado." << v << " = " << visitado[v] << ", low." << v << " = " << low[v] << endl;
    cout << "Pila: ";
    stack<pair<char, char>> temp = pila;
    while (!temp.empty()) {
        cout << "(" << temp.top().first << ", " << temp.top().second << ") ";
        temp.pop();
    }
    cout << endl;

    for(char w : adj[v]){
        cout << "\nw: " << w << ", v: " << v << endl;
        if(visitado[w] == -1){
            padre[w] = v;
            numHijos++;
            pila.push({v, w});
            bcAux(w);
            low[v] = min(low[v], low[w]);
            cout << "  Ahora low." << v << " = min(" << low[v] << ", " << low[w] << ") = " << low[v] << endl;
            
            if((padre[v] == -1 && numHijos > 1) || (padre[v] != -1 && low[w] >= visitado[v])){
                comps.push_back(vector<pair<char, char>>());
                cout << "  Creando nueva componente biconexa debido a punto de articulación en " << v << endl;
                
                while(pila.top() != make_pair(v, w)){
                    comps.back().push_back(pila.top());
                    cout << "  Moviendo arista w: " << pila.top().first << ", v: " << pila.top().second << " a la componente" << endl;
                    pila.pop();
                }
                comps.back().push_back(pila.top());
                cout << "  Moviendo arista final w: " << pila.top().first << ", v: " << pila.top().second << " a la componente" << endl;
                pila.pop();
            }
        }
        else if(w != padre[v]){
            low[v] = min(low[v], visitado[w]);
            cout << "  Retroceso encontrado: (w: " << w << ", v: " << v << ") actualiza low." << v << " a " << low[v] << endl;
            if(visitado[w] < visitado[v]){
                pila.push({v, w});
                cout << "  Agregando arista de retroceso w: " << v << ", v: " << w << " a la pila" << endl;
            }
        } else {
            cout << "  No se cumple ninguna condición y se continua" << endl;
        }
    }
    cout << "\nSaliendo de bcAux(" << v << ")\n";
}

void bcTarjan(){
    t = 0;
    cout << "\nIniciando Tarjan" << endl;
    for(auto& p : adj){
        visitado[p.first] = low[p.first] = padre[p.first] = -1;
    }

    for(auto& p : adj){
        if(visitado[p.first] == -1){
            cout << "\nLlamando bcAux(" << p.first << ") desde bcTarjan" << endl;
            bcAux(p.first);

            if(!pila.empty()){
                comps.push_back(vector<pair<char, char>>());
                cout << "  Procesando pila final para componentes restantes" << endl;
                while(!pila.empty()){
                    comps.back().push_back(pila.top());
                    pila.pop();
                }
            }
        }
    }
}

int main(){
    adj = {
        {'a', {'b', 'c'}},
        {'b', {'d', 'a', 'c'}},
        {'c', {'a', 'b'}},
        {'d', {'j', 'e', 'k', 'b'}},
        {'j', {'d', 'l'}},
        {'l', {'j', 'k'}},
        {'k', {'l', 'd'}},
        {'e', {'d', 'g'}},
        {'g', {'e', 'f', 'h'}},
        {'f', {'g', 'h', 'i'}},
        {'h', {'i', 'g', 'f'}},
        {'i', {'f', 'h'}}
    };

    bcTarjan();
    
    cout << "\nTotal de Componentes Biconexos: " << comps.size() << endl;
    for(int i = 0; i < comps.size(); ++i){
        cout << "Componente " << i + 1 << ":";
        for(auto& edge : comps[i])
            cout << " (w: " << edge.first << ", v: " << edge.second << ")";
        cout << endl;
    }
    
    return 0;
}
