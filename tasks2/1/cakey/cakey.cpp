#include <cstdio>

int main() {
    int N, M;

    // Leer hasta EOF
    while (scanf("%d", &N) != EOF) {
        scanf("%d", &M);

        int entryTimes[N], exitTimes[M];

        // Leer los tiempos de entrada
        printf("Tiempos de entrada:\n");
        for (int i = 0; i < N; ++i) {
            scanf("%d", &entryTimes[i]);
            printf("%d ", entryTimes[i]); // Verificación
        }
        printf("\n");

        // Leer los tiempos de salida
        printf("Tiempos de salida:\n");
        for (int i = 0; i < M; ++i) {
            scanf("%d", &exitTimes[i]);
            printf("%d ", exitTimes[i]); // Verificación
        }
        printf("\n");
    }

    return 0;
}
