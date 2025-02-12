/*
Jose David Ruano Burbano 8982982
Tarea 2 - triangle
Arboles y grafos 2025-1

Analisis de complejidad:

La complejidad temporal de este algoritmo es O(log n), 
donde n es el tamaño del intervalo inicial dividido por la precisión eps,
esto se debe a que el metodo de bisección reduce el intervalo 
de busqueda a la mitad en cada iteración. Con esto la complejidad seria O(log ab/eps)
*/
#include <cmath>
#include <cstdio>
double ratio(double ad, double ab) {
    double x = ad / ab, ratio;
    ratio = (x *x) / (1 - x*x);
    return ratio;
}

int main() {
    int t;
    double ab, ac, bc, r, eps = 1e-10 ;
    scanf("%d", &t);

    for (int i = 1; i <= t; ++i) {
        scanf("%lf %lf %lf %lf", &ab, &ac, &bc, &r);
        double low = 0, high = ab, mid;

        while (high-low > eps) {
            mid = (low + high)/2;
            if (ratio(mid, ab) < r) {
                low = mid;
            } else {
                high = mid;
            }
        }
        printf("Case %d: %.6f\n", i, mid);
    }

    return 0;
}