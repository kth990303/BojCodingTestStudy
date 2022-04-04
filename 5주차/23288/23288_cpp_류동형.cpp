#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int map[21][21];
int check[21][21];
int dice[7];
int dir = 1;//처음이동방향 동쪽 
int visit[21][21];
int n, m, k; //세로, 가로, 이동횟수
int real_map[21][21];//이동할수있는칸의수 c가 들어있는맵
int nx = 1;
int ny = 1;
int answer = 0;

void change_check(int x, int y, int temp, int cnt) {//각 칸에서 갈 수 있는 칸 수 구하기
    if (x <= 0 || y <= 0 || x > n || y > m || visit[x][y] == 1) {
        return;
    }

    if (map[x][y] == temp && visit[x][y] == 0) {
        visit[x][y] = 1;
        check[x][y] = cnt;
        change_check(x + 1, y, temp, cnt);
        change_check(x, y + 1, temp, cnt);
        change_check(x - 1, y, temp, cnt);
        change_check(x, y - 1, temp, cnt);
    }
}

void change_dice_dir() {
    if (dir == 1) {
        ny++;
        if (nx <= 0 || ny <= 0 || nx > n || ny > m) {
            dir = 3;
            ny--;
            ny--;
        }
    }
    else if (dir == 2) {
        nx++;
        if (nx <= 0 || ny <= 0 || nx > n || ny > m) {
            dir = 4;
            nx--;;
            nx--;
        }
    }
    else if (dir == 3) {
        ny--;
        if (nx <= 0 || ny <= 0 || nx > n || ny > m) {
            dir = 1;
            ny++;
            ny++;
        }
    }
    else if (dir == 4) {
        nx--;
        if (nx <= 0 || ny <= 0 || nx > n || ny > m) {
            dir = 2;
            nx++;
            nx++;
        }
    }
}

void solve() {
    change_dice_dir();

    //이동방향으로 한칸굴러가기
    int temp_dice[7];
    for (int i = 1; i <= 6; i++) {
        temp_dice[i] = dice[i];
    }
    if (dir == 1) { dice[1] = temp_dice[4]; dice[2] = temp_dice[2]; dice[3] = temp_dice[1]; dice[4] = temp_dice[6]; dice[5] = temp_dice[5]; dice[6] = temp_dice[3]; }
    if (dir == 2) { dice[1] = temp_dice[2]; dice[2] = temp_dice[6]; dice[3] = temp_dice[3]; dice[4] = temp_dice[4]; dice[5] = temp_dice[1]; dice[6] = temp_dice[5]; }
    if (dir == 3) { dice[1] = temp_dice[3]; dice[2] = temp_dice[2]; dice[3] = temp_dice[6]; dice[4] = temp_dice[1]; dice[5] = temp_dice[5]; dice[6] = temp_dice[4]; }
    if (dir == 4) { dice[1] = temp_dice[5]; dice[2] = temp_dice[1]; dice[3] = temp_dice[3]; dice[4] = temp_dice[4]; dice[5] = temp_dice[6]; dice[6] = temp_dice[2]; }

    //점수 획득하기
    answer = map[nx][ny] * real_map[nx][ny] + answer;

    //방향결정
    if (dice[6] > map[nx][ny]) {
        if (dir == 4) { dir = 1; }
        else { dir++; }
    }
    else if (dice[6] < map[nx][ny]) {
        if (dir == 1) { dir = 4; }
        else { dir--; }
    }
    else if (dice[6] == map[nx][ny]) {}
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    cin >> n >> m >> k;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> map[i][j];
        }
    }

    for (int i = 1; i <= 6; i++) {
        dice[i] = i;
    }//초기 주사위의 값 대입

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            change_check(i, j, map[i][j], i * m + j);
        }
    }//같은 숫자가 연속되는 친구들 전부 i*m+j의 값으로 너어서 표시


    for (int l = 0; l <= n * m + m; l++) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (check[i][j] == l) {
                    count++;
                }
            }
        }// 같은 값가지는 애들 count
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (check[i][j] == l) {
                    real_map[i][j] = count;
                }
            }//그 count 값을 대입
        }
    }//real_map구하는과정

    for (int i = 1; i <= k; i++) {
        solve();
    }

    cout << answer;
}