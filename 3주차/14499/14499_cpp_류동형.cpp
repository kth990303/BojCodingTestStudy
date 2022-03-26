#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int N, M, x, y, k; //세로, 가로, 주사위 좌표, 명령 개수
int map[21][21]; //지도
int order[1001]; // 명령개수저장
int dice[7]; //주사위 
int temp[7]; //잠시 저장할 배열

int dx[4] = { 0,0,-1,1 }; //각각 동 서 북 남
int dy[4] = { 1,-1,0,0 };

void solve(int n) {
    for (int i = 1; i <= 6; i++) {
        temp[i] = dice[i];
    }//temp 배열에 주사위 값들 저장

    int nx = x + dx[n - 1];
    int ny = y + dy[n - 1];

    if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
        return;
    }//주사위가 이동했는데 바깥으로 이동할시 명령 무시

    x = nx;
    y = ny; //주사위 좌표값 이동

    if (n == 1) {//동쪽으로 굴렀을때
        dice[1] = temp[4];
        dice[2] = temp[2];
        dice[3] = temp[1];
        dice[4] = temp[6];
        dice[5] = temp[5];
        dice[6] = temp[3];
        if (map[x][y] == 0) { //주사위 바닥에 수가 0이면 주사위 값이 맵으로이동
            map[x][y] = dice[6];
            cout << dice[1] << "\n";
            return;
        }
        else {
            dice[6] = map[x][y]; //0이 아닌경우는 칸에 쓰인수가 주사위 바닥으로
            map[x][y] = 0; //그리고 맵에는 0저장
            cout << dice[1] << "\n";
            return;
        }
    }
    if (n == 2) {//서쪽
        dice[1] = temp[3];
        dice[2] = temp[2];
        dice[3] = temp[6];
        dice[4] = temp[1];
        dice[5] = temp[5];
        dice[6] = temp[4];
        if (map[x][y] == 0) {
            map[x][y] = dice[6];
            cout << dice[1] << "\n"; return;
        }
        else {
            dice[6] = map[x][y];
            map[x][y] = 0;
            cout << dice[1] << "\n"; return;
        }
    }
    if (n == 3) {//북쪽으로
        dice[1] = temp[2];
        dice[2] = temp[6];
        dice[3] = temp[3];
        dice[4] = temp[4];
        dice[5] = temp[1];
        dice[6] = temp[5];
        if (map[x][y] == 0) {
            map[x][y] = dice[6];
            cout << dice[1] << "\n"; return;
        }
        else {
            dice[6] = map[x][y];
            map[x][y] = 0;
            cout << dice[1] << "\n"; return;
        }
    }
    if (n == 4) {
        dice[1] = temp[5];
        dice[2] = temp[1];
        dice[3] = temp[3];
        dice[4] = temp[4];
        dice[5] = temp[6];
        dice[6] = temp[2];
        if (map[x][y] == 0) {
            map[x][y] = dice[6];
            cout << dice[1] << "\n"; return;
        }
        else {
            dice[6] = map[x][y];
            map[x][y] = 0;
            cout << dice[1] << "\n"; return;
        }
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> M >> x >> y >> k;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
        }
    }

    for (int i = 0; i < k; i++) {
        cin >> order[i];
    }

    for (int i = 0; i < k; i++) {
        solve(order[i]);
    }
}