/* 
Jose David Ruano Burbano
Parcial 1 - Parte practica - Slowcalm
Arboles y grafos 2024-2
Universidad Pontificia Javeriana cali
*/

#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

double T(double n, vector<pair<double,double>> & v, double y){
    int i;
    double time = 0; 
    bool flag = true;
    for(i = 0; i < n && flag; i++){
        if (v[i].second + y <= 0) {
            time = 1e18; // Velocidad no válida, usamos un valor grande para no afectar la bisección
            flag = false; // Terminar el ciclo para no seguir sumando    
        } 
        else {
            time += v[i].first / (v[i].second + y);    
        }
    }
    return time;
}

int main() {
    double t, m, di, si;
    const double EPS = 1e-11;
    // Leer la entrada
    while (cin >> m >> t) {

        vector<pair<double, double>> v; // Vector para tener los di y si
        double min_si; // Para encontrar la distancia máxima
        // Leer los valores de di y si
        for (int i = 0; i < m; i++) {
            cin >> di >> si;
            min_si = si;
            v.push_back(make_pair(di, si));

            if (si < min_si)  min_si = si;
        }
        // Método de bisección
        double low = min_si*-1, hi = 1e6, mid;
        while (hi - low > EPS) {
            mid = (low + hi) / 2;
            if (T(m, v, mid) > t) {
                low = mid;
            } 
            else {
                hi = mid;
            }
        }
        // Imprimir y
        printf("%.6f\n", mid);
        
    }
    return 0;
}



