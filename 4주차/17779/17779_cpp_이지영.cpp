#include <iostream>
#include <algorithm>
#include<cstring>
#include <cmath>
using namespace std;

int N;
int A[21][21] = { 0 }; //재현시 각 구역의 인구
int visit[21][21] = { 0 };//선거구 번호 입력
int gapp = 999999; //선거구당 인구 차이의 최솟값 출력용

void getgap() {
    //4. 선거구 별 인구차이 구하기
    int jh[6] = { 0 };//재현의 jh: 각 선거구별 인구 저장
    int minn = 9999999; //틀린 원인이 된 코드
    int maxx = 0; // 0<A[r][c]<101
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (visit[i][j] == 1) jh[1] += A[i][j];
            if (visit[i][j] == 2) jh[2] += A[i][j];
            if (visit[i][j] == 3) jh[3] += A[i][j];
            if (visit[i][j] == 4) jh[4] += A[i][j];
            if (visit[i][j] == 5) jh[5] += A[i][j];
        }
        //셀프pr: 큰 차이 없을 것 같지만 switch 문을 쓸지 if문을 쓸지 성능차이 알아보기
    }
    for (int i = 1; i <= 5; i++) {
        if (minn > jh[i]) {
            minn = jh[i];
        }
        if (maxx < jh[i]) {
            maxx = jh[i];
        }
    }
    if (gapp > maxx - minn) {
        gapp = maxx - minn;
        //for (int i = 1; i <= 5; i++) { cout << jh[i]; }
    }
}
void grid(int x, int y, int d1, int d2) {
    memset(visit, 0, sizeof(visit));

    //1. 경계선 5번 선거구로 세팅
    for (int i = 0; i <= d1; i++) {
        visit[x + i][y - i] = 5;
        visit[x + d2 + i][y + d2 - i] = 5;
    }
    for (int i = 0; i <= d2; i++) {
        visit[x + i][y + i] = 5;
        visit[x + d1 + i][y - d1 + i] = 5;
    }

    //2. 경계선 안쪽 5번 선거구로 세팅
    for (int i = x + 1; i < x + d1 + d2; i++) {
        bool switchh = false;
        //switchh의 값 리셋
        for (int j = 1; j <= N; j++) {
            if (visit[i][j] == 5) {
                //경계선을 만나면 switchh의 값 바꾸기
                switchh = switchh ? false : true;
            }
            if (switchh) {
                //switchh가 true일때 경계선 안쪽으로 들어왔다고 가정하고
                //5번 선거구로 세팅
                visit[i][j] = 5;
            }
        }
    }
    //3. 나머지 선거구 번호 입력
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (visit[i][j] != 5 && i >= 1 && i < x + d1 && 1 <= j && j <= y) {
                visit[i][j] = 1;
                continue;
            }
            if (visit[i][j] != 5 && i >= 1 && i <= x + d2 && y < j && j <= N) {
                visit[i][j] = 2;
                continue;
            }
            if (visit[i][j] != 5 && x + d1 <= i && i <= N && 1 <= j && j < y - d1 + d2) {
                visit[i][j] = 3;
                continue;
            }
            if (visit[i][j] != 5 && x + d2 < i && i <= N && y - d1 + d2 <= j && j <= N) {
                visit[i][j] = 4;
                continue;
            }
        }
    }
    //4. 선거구 별 인구차이 구하기
    getgap();
}
int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> A[i][j];
        }
    }
    //0. x, y, d1, d2를 부르트 포스로 다 대입
    for (int a = 1; a <= N - 2; a++) {
        for (int b = 2; b <= N - 1; b++) {
            for (int c = 1; a + c <= N - 2 && b - c >= 1; c++) {
                for (int d = 1; a + c + d <= N && b + d <= N; d++) {
                    grid(a, b, c, d);
                }
            }
        }
    }

    //5. 답 출력
    cout << gapp;
}