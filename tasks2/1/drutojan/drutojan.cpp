#include <queue>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    int t, m, n, k;
    string name, inSeat;

    cin >> t;
    for (int c = 1; c <= t; ++c) {
        cin >> m >> n >> inSeat;
        unordered_map<string, pair<int, queue<string>>> times = {
            {"Ja", {0, queue<string>()}},
            {"Sam", {0, queue<string>()}},
            {"Sha", {0, queue<string>()}},
            {"Sid", {0, queue<string>()}},
            {"Tan", {0, queue<string>()}}
        };
        queue<string> lists[5];

        for (int l = 0; l < 5; ++l) {
            cin >> k;
            for (int i = 0; i < k; ++i) {
                cin >> name;
                lists[l].push(name);
            }
        }

        times["Ja"].second = lists[0];
        times["Sam"].second = lists[1];
        times["Sha"].second = lists[2];
        times["Sid"].second = lists[3];
        times["Tan"].second = lists[4];

        int time = 0;
        bool flag = true;

        while (flag) {
            if (time + m > n) { 
                times[inSeat].first += (n - time);
                time = n;
                flag = false;
            } else {
                times[inSeat].first += m;
                time += m;
            }

            if (time < n) {
                time += 2; // Tiempo de intercambio

                if (time >= n) {
                    flag = false;
                } else {
                    string next = times[inSeat].second.front();
                    times[inSeat].second.pop();
                    times[inSeat].second.push(next);
                    inSeat = next;
                }
            }
        }

        cout << "Case " << c << ":" << endl;
        cout << "Ja " << times["Ja"].first << endl;
        cout << "Sam " << times["Sam"].first << endl;
        cout << "Sha " << times["Sha"].first << endl;
        cout << "Sid " << times["Sid"].first << endl;
        cout << "Tan " << times["Tan"].first << endl;
    }
    return 0;
}
