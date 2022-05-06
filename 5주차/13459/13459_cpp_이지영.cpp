#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

int N, M;
char A[10][10]; //보드 문자 입력 위해 char형
bool endd;

struct xy {
    int x, y;
};
xy inp;//input 약자
vector<xy> r;
vector<xy> b;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 }; //좌 하 우 상


bool escape(int cnt, int rx, int ry, int bx, int by) {
    if (cnt > 10) { return endd; } //10번 이상 이동
    //int rx = r[0].x; int ry = r[0].y;
    //int bx = b[0].x; int by = b[0].y; //지역변수에 위치 다시 넣기

    for (int i = 0; i < 4; i++) {
        bool r_end = false, b_end = false;
        int nrx = rx, nry = ry, nbx = bx, nby = by;

        while (1) {
            //기울이면 끝까지 이동
            if (A[nry + dy[i]][nrx + dx[i]] == '.') { nrx += dx[i]; nry += dy[i]; }
            else if (A[nry + dy[i]][nrx + dx[i]] == 'O') { r_end = true; nrx += dx[i]; nry += dy[i]; break; }
            else if (A[nry + dy[i]][nrx + dx[i]] == '#') { break; }
        }
        while (1) {
            //기울이면 끝까지 이동
            if (A[nby + dy[i]][nbx + dx[i]] == '.') { nbx += dx[i]; nby += dy[i]; }
            else if (A[nby + dy[i]][nbx + dx[i]] == 'O') { b_end = true; nbx += dx[i]; nby += dy[i]; break; }
            else if (A[nby + dy[i]][nbx + dx[i]] == '#') { break; }
        }
        if (b_end) { continue; }
        else if (r_end) { endd = true; return endd; }

        if (nrx == nbx && nry == nby) {
            if (i == 0) {
                (ry > by)?nry += 1:nby += 1;
                //빨간공이 더 밑에서 시작
            }
            else if (i == 1) {
                (rx > bx)?nbx -= 1:nrx -= 1;
                //파란공이 더 왼쪽에서 시작
            }
            else if (i == 2) {
                (ry > by)?nby -= 1:nry -= 1;
                //파란공이 더 위에서 시작
            }
            else if (i == 3) {
                (rx > bx)?nrx += 1:nbx += 1;
                //빨간공이 더 오른쪽에서 시작
            }
        }
        escape(cnt + 1, nrx, nry, nbx, nby); //변화된 값으로 백트래킹

    }
    return endd;
}
int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;//세로 가로

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> A[i][j];
            if (A[i][j] == 'R') { inp.x = j; inp.y = i; r.push_back(inp); A[i][j] = '.'; }
            else if (A[i][j] == 'B') { inp.x = j; inp.y = i; b.push_back(inp); A[i][j] = '.'; }
            //r, b 위치 저장하고 다시 .으로 설정
        }
    }
    escape(1, r[0].x, r[0].y, b[0].x, b[0].y) ? cout << 1 : cout << 0; //성공하면 1 아니면 0
    return 0;
}