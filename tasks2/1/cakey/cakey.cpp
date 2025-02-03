/* Jose David Ruano Burbano 8982982 */
#include <cstdio>
#include <unordered_map>
using namespace std;
int main() {
    int n, m;

    while (scanf("%d", &n) != EOF) {
        scanf("%d", &m);

        int entryTimes[n], exitTimes[m];
        for (int i = 0; i < n; ++i) {
            scanf("%d", &entryTimes[i]);
        }
        for (int i = 0; i < m; ++i) {
            scanf("%d", &exitTimes[i]);
        }

        unordered_map<int, int> count;
        int max_freq = 0;
        int best_time = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int diff = exitTimes[j] - entryTimes[i];
                if (diff >= 0) {
                    count[diff]++;
                    if (count[diff] > max_freq || (count[diff] == max_freq && diff < best_time)) {
                        max_freq = count[diff];
                        best_time = diff;
                    }
                }
            }
        }

        printf("%d\n", best_time);
    }

    return 0;
}
