/*
Jose David Ruano Burbano
Tarea 2 - Bids
Arboles y grafos 2024-2

Analisis de complejidad:
La complejidad temporal de este algoritmo es O((p + c) * log(p + c)), donde p es el número de productores,
y c es el número de consumidores. Esto se debe a que ordenamos las listas de productores y consumidores
(O(p log p + c log c)), y luego realizamos búsquedas binarias (O(log p + log c)) para cada uno de los p + c valores posibles.
*/

#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;


int serchForProducers(const vector<int>& vec, int value) {
    // funcion para buscar el primer valor mayor o igual al valor dado
    int l = 0;
    int r = vec.size();
    
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (vec[mid] <= value) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}

int serchForConsumers(const vector<int>& vec, int value) {
    // funcion para buscar el primer valor mayor al valor dado
    int l = 0;
    int r = vec.size();
    
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (vec[mid] < value) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}


int main(){
    int t;   // numero de casos de prueba
    int p , c;  // p - numero de productores, c - numero de consumidores

    cin >> t;
    for(int i = 0; i < t; i++){
        bool flag = true;
        cin >> p >> c;

        vector<int> producers(p);
        vector<int> consumers(c);
        vector<int> totalBids;

        // leer los precios ideales de los productores y consumidores
        for(int j = 0; j < p; j++){
            cin >> producers[j];
            totalBids.push_back(producers[j]);
        }
        for(int j = 0; j < c; j++){
            cin >> consumers[j];
            totalBids.push_back(consumers[j]);
        }
        totalBids.push_back(0); // Agregamos el caso del 0 para que tambien se tenga en cuenta
        // Ordenamos las ofertas para poder aplicar la busqueda binaria 
        sort(producers.begin(), producers.end());
        sort(consumers.begin(), consumers.end());

        if (producers.empty()){
            cout << "0 0" << endl;
        }
        else if (consumers.empty()){
            cout << producers[producers.size()-1] << " 0" << endl;
        }
        else{
            int idealBid = 1e8 , idealAngry = 1e8;
            for (int j = 0; j < totalBids.size() && flag; j++){
                // Encontrar la poscicion correspondiente con busqueda binaria segun el valor dado de los productores y consumidores
                int pos = serchForProducers(producers, totalBids[j]); 
                int pos2 = serchForConsumers(consumers, totalBids[j]);
                // Calcular los enojados totales 
                int totalAngry = producers.size() - pos;
                totalAngry = totalAngry + pos2;
                
                // Encontrar la mejor oferta y la cantidad de enojados ideal
                if (totalAngry == idealAngry && idealBid >= totalBids[j]){
                    idealBid = totalBids[j];
                }
                else if (idealAngry > totalAngry){
                    idealBid = totalBids[j];
                    idealAngry = totalAngry;
                } 
                
            }
            cout << idealBid << " " << idealAngry << endl;
        }
        
    }

    return 0; 
}