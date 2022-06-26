#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
//1. 뭐가 섬인지
//2. BFS
int N;
int ans = INT_MAX;
int A[100][100];
bool visitt[100][100];


struct xy {
    int x, y;
};
xy point;
vector<xy> map;
int dx[4] = { 0, 0, 1, -1};
int dy[4] = { 1, -1, 0, 0};

void clustering(){
    //같은 대륙들 표시
    int mapping = 1;
}

int main(void)
{

    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N ;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
            if (A[i][j] == '1') { point.x = i; point.y = j; map.push_back(point); A[i][j] = INT_MIN; }
        }
    }
    return 0;
}