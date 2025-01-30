#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    
    int n, m;
    vector<int> entryTimes, exitTimes;

    while(scanf("%d", &n) != EOF){
        scanf("%d", &m);

        for(int i = 0; i < n; ++i){
            scanf("%d", &entryTimes[i]);
        }
        for(int i = 0; i < n; ++i){
            scanf("%d", &exitTimes[i]);
        }
    
    }
    


    return 0;   
}