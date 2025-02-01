#include <queue>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int t, m, n, k;
    string name, inSeat;
    queue<string> lists[5];  // Ja, Sam, Sha, Sid, Tan

    cin >> t;
    for (int c = 1; c <= t; ++c) {
        cin >> m >> n >> inSeat;

        for (int l = 0; l < 5; ++l) {
            cin >> k;
            for (int i = 0; i < k; ++i) {
                cin >> name;
                lists[l].push(name);  
            }
        }

    }

    return 0;

}