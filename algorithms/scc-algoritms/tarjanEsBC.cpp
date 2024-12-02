/*
Algoritmo para verificar si un grafo es biconexo

Autor: Carlos Ramirez
Fecha: Septiembre 19 de 2024

*/

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int n, t;
vector<vector<int> > adj(50000);
int visitado[50000];
int low[50000];
int padre[50000];

bool tieneAPAux(int);

bool esBiconexo(){
  int i;

  for(i = 0; i < n; i++)
    low[i] = visitado[i] = padre[i] =-1;

  if(tieneAPAux(0))
    return false;
  
  for(i = 0; i < n; i++)
    if(visitado[i] == -1)
      return false;

  return true;
}

bool tieneAPAux(int v){
  int w, numHijos = 0;
  visitado[v] = low[v] = ++t;
  bool ans = false;

  for(int i = 0; i < adj[v].size() && !ans; i++){
    w = adj[v][i];
    if(visitado[w] == -1){
      numHijos++;
      padre[w] = v;
      
      if(tieneAPAux(w))
	ans = true;
      else{
	low[v] = low[v] < low[w] ? low[v] : low[w];

        //verificar si es un punto de articulacion
        if(padre[v] != -1 && low[w] >= visitado[v])
	  ans = true;
      }
    }
    else if(w != padre[v])
      low[v] = low[v] < visitado[w] ? low[v] : visitado[w];
  }

  if(padre[v] == -1 && numHijos > 1)
    ans = true;
  
  return ans;
}

int main(){
  int m, i, aux1, aux2;
  bool res;
  
  cin >> n >> m;

  for(i = 0; i < m; i++){
    cin >> aux1 >> aux2;
    adj[aux1].push_back(aux2);
    adj[aux2].push_back(aux1);
  }

  res = esBiconexo();

  if(res)
    cout << "El grafo es biconexo" << endl;
  else
    cout << "El grafo no es biconexo" << endl;
  
  return 0;
}
