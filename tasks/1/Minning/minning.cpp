#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int S, W, C, K, M;
    while (cin >> S >> W >> C >> K >> M){
        // cout << S << " " << W << " " << C << " " << K << " " << M << endl;
        int totalTimeRobotsProduction = M * K;
        int timeRobotAux = 0;
        int time = 0;
        int units = 0;
        for (int i = 0; units < 10000; i++){
            if (timeRobotAux < totalTimeRobotsProduction){
                timeRobotAux += M;
                time += S + W + M;
            } 
            else {
                time += S + W;
            }
            units += C;
            
            time += S;
            
            
        }
        cout << time << endl;
    }
    return 0;
}