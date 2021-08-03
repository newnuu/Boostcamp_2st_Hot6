#include <iostream>
#include <stdio.h>
#include <math.h>
#define MAX 51
using namespace std;

int n, m, ans;
int map[MAX][MAX];

void solve(int x, int y) {
    int i = 0;
    
    while(1){
        int nx = x + i;
        int ny = y + i;
        
        if(nx >= n || ny >= m) break;
        
        if(map[x][y] == map[nx][y] && map[x][y] == map[x][ny] && map[x][y] == map[nx][ny]){
            ans = max(ans, (i+1) * (i+1));
        }
        
        i++;
    }
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%1d", &map[i][j]);
        }
    }
    
    ans = 0;
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            solve(i, j);
        }
    }
    
    cout << ans << "\n";
}
