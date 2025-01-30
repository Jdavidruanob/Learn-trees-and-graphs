#include <cstdio>
#include <stack>
#include <tuple>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    
    while (n != 0) {
        stack<tuple<int, int, vector<int>>> s;
        stack<vector<int>> factorizations;
        
        s.push(make_tuple(n, 2, vector<int>()));

        while (!s.empty()) {
            tuple<int, int, vector<int>> current = s.top();
            int actual = get<0>(current);
            int start = get<1>(current);
            vector<int> factors = get<2>(current);  // Copia del vector de factores actuales
            
            s.pop();  // Removemos el nodo actual después de procesarlo

            if (actual == 1 && factors.size() > 1) {
                factorizations.push(factors);
                continue;
            }

            // Probar divisores desde 'start' hasta sqrt(actual)
            for (int i = start; i <= sqrt(actual); ++i) {
                if (actual % i == 0) {
                    vector<int> new_factors = factors;
                    new_factors.push_back(i);
                    s.push(make_tuple(actual / i, i, new_factors));
                }
            }

            // Caso especial: agregar el factor restante si es mayor que el último factor probado
            if (actual >= start && !factors.empty()) {
                factors.push_back(actual);
                factorizations.push(factors);
            }
        }

        // Imprimir el número de factorizaciones
        printf("%lu\n", factorizations.size());

        // Imprimir cada factorización correctamente
        while (!factorizations.empty()) {
            vector<int> vec = factorizations.top();
            factorizations.pop();

            for (int i = 0; i < vec.size(); ++i) {
                if (i > 0) printf(" ");
                printf("%d", vec[i]);
            }
            printf("\n");
        }

        scanf("%d", &n);
    }

    return 0;
}
