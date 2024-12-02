/*
Jose David Ruano Burbano
Tarea 2 - Ladders
Arboles y grafos 2024-2

Análisis de complejidad:
La complejidad temporal de este algoritmo es O(log n), donde n es el tamaño del intervalo inicial dividido por la precisión eps.
Esto se debe a que el método de bisección reduce el intervalo de búsqueda a la mitad en cada iteración.
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Función que calcula la altura de la escalera en función del ancho de la calle
double height(double l, double w) {
    return sqrt(l * l - w * w);
}

// Función que calcula c
double Cross(double x, double y, double w) {
    double c = 0, h1 = height(x, w), h2 = height(y, w);
    c = (h1 * h2) / (h1 + h2);
    return c;
}

int main() {
    double x, y, c;
    while (cin >> x >> y >> c) {
        double low = 0, high = min(x, y), mid;
        const double eps = 1e-8;

        // Método de bisección
        while (high - low > eps) {
            mid = (low + high) / 2;
            if (Cross(x, y, mid) >= c) {
                low = mid;
            } else {
                high = mid;
            }
        }

        printf("%.3f\n", mid);
    }

    return 0;
}

