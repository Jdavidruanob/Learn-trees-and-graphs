/*
Algoritmo de Tarjan (Componentes biconexos)
Autor: Carlos Ramirez
Fecha: Septiembre 19 de 2024

 */

#include <vector>
#include <stack>
#include <iostream>
#include <set>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int low[50000];
int padre[50000];
vector<vector<pair<int, int> > > comps;
stack<pair<int, int>> pila;

void bcAux(int);

void bcTarjan(){
  int i;

  for(i = 0; i < n; i++)
    low[i] = visitado[i] = padre[i] = -1;

  for(i = 0; i < n; i++){
    if(visitado[i] == -1)
      bcAux(i);

    if(!pila.empty()){
      comps.push_back(vector<pair<int, int> >());

      while(!pila.empty()){
	comps[comps.size() - 1].push_back(pila.top());
	pila.pop();
      }
    }
  }
}

void bcAux(int v){
  int w, numHijos;
  visitado[v] = low[v] = ++t;
  numHijos = 0;

  for(int i = 0; i < adj[v].size(); i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      padre[w] = v;
      numHijos++;
      pila.push(make_pair(v, w));
      bcAux(w);
      low[v] = low[v] < low[w] ? low[v] : low[w];

      //verificar si es un punto de articulacion
      if((padre[v] == -1 && numHijos > 1) || (padre[v] != -1 && low[w] >= visitado[v])){
	comps.push_back(vector<pair<int, int> >());

	while(pila.top().first != v || pila.top().second != w){
	  comps[comps.size() - 1].push_back(pila.top());
	  pila.pop();
	}

	comps[comps.size() - 1].push_back(pila.top());
	pila.pop();
      }
    }
    else if(w != padre[v]){
      low[v] = low[v] < visitado[w] ? low[v] : visitado[w];

      if(visitado[w] < visitado[v])
	pila.push(make_pair(v, w));
    }
  }
}

int main(){
  int m, i, j, aux1, aux2;

  cin >> n >> m;

  for(i = 0; i < m; ++i){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
  }

  bcTarjan();
  
  cout << "Total de Componentes Biconexos: " << comps.size() << endl;
  for(i = 0; i < comps.size(); ++i){
    cout << "Componente " << i + 1 << ":";
    for(j = 0; j < comps[i].size(); ++j)
      cout << " (" << comps[i][j].first << ", " << comps[i][j].second << ")";
    cout << endl;
  }
  
  return 0;
}
