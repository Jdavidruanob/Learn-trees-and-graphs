/*
Tarea 6
Arboles y grafos 
Jose David Ruano Burbano 
8982982

Analisis complejidad:

n es el numero de elementos en el arreglo.
q es el numero de operaciones de consulta y desplazamiento.

- Construccion del arbol segmentado O(n)
- Consulta en un rango usando el arbol segmentado O(log n)
- Actualizacion de un elemento en el arbol segmentado O(log n)
- Desplazamiento circular de elementos O(k log n) siendo k es el numero de elementos en el subconjunto desplazado

Por lo tanto:
La complejidad total de la solucion es O(n + q log n) respecto al numero de elementos n y el numero de operaciones q.
*/ 

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <limits.h>

using namespace std;
int n;
vector<int> tree;

void build(vector<int>& a, int v, int l, int r) {
    if (l == r) 
        tree[v] = a[l];
    else{
        int m = l + ((r - l) >> 1);
        build(a, v + 1, l, m);
        build(a, v + 2 * (m - l + 1), m + 1, r);
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - l + 1)]);
    }
}

int query(int v, int L, int R, int l, int r) {
    int ans;
    if (l > r) 
        ans = INT_MAX;
    else if (l == L && r == R) 
        ans = tree[v];
    else {
        int m = L + ((R - L) >> 1);
        ans = min(query(v + 1, L, m, l, min(r, m)), query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r));
    }
    return ans;
}

void update(int v, int L, int R, int pos, int h) {
    if (L == R) 
        tree[v] = h;
    else {
        int m = L + ((R - L) >> 1);
        if (pos <= m)
            update(v + 1, L, m, pos, h);
        else
            update(v + 2 * (m - L + 1), m + 1, R, pos, h);
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - L + 1)]);
    }
}

void Shift(vector<int>& A, vector<int>& indices) {
    int aux = A[indices[0]]; 
    for (int i = 0; i < indices.size()-1; i++) {
        A[indices[i]] = A[indices[i+1]]; 
        update(0, 0, n- 1, indices[i], A[indices[i]]);  
    }
    A[indices[indices.size()-1]] = aux;  
    update(0, 0, n - 1, indices[indices.size()-1], aux); 
}

int main() {
    int q;
    cin >> n >> q;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    tree.resize(n*2);
    build(A, 0, 0, n - 1);
    string operation;
    for (int i = 0; i <= q; ++i) {
        getline(cin, operation);
        if (operation.substr(0, 5) == "query") {
            int l, r;
            sscanf(operation.c_str(), "query(%d,%d)", &l, &r);
            l--; 
            r--; 
            cout << query(0, 0, n - 1, l, r) << endl;

        } else if (operation.substr(0, 5) == "shift") {
            vector<int> indices;
            int indice;
            stringstream num(operation.substr(6));
            while (num >> indice) {
                indices.push_back(indice- 1);
                if (num.peek() == ',') {
                    num.ignore();
                }
            }
            Shift(A, indices);
        }
    }
    return 0;
}