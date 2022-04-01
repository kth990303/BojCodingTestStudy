#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
int N;
int map[21][21];
int answer = 999999999;
int check[21][21];

void check1() {
    int a[6];
    for (int i = 0; i <= 5; i++) {
        a[i] = 0;
    }
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (check[i][j] == 1) a[1] = a[1] + map[i][j];
            if (check[i][j] == 2) a[2] = a[2] + map[i][j];
            if (check[i][j] == 3) a[3] = a[3] + map[i][j];
            if (check[i][j] == 4) a[4] = a[4] + map[i][j];
            if (check[i][j] == 5) a[5] = a[5] + map[i][j];
        }
    }
    int min = 999999999;
    int max = -999999999;
    for (int i = 1; i <= 5; i++) {
        if (min > a[i]) {
            min = a[i];
        }
        if (max < a[i]) {
            max = a[i];
        }
    }

    if (answer > max - min) {
        answer = max - min;
    }
}

void solve() {
    for (int x = 1; x <= N - 2; ++x) {
        for (int y = 2; y <= N - 1; ++y) {
            for (int d1 = 1; x + d1 <= N - 2 && y - d1 >= 1; ++d1) {
                for (int d2 = 1; x + d1 + d2 <= N && y + d2 <= N; ++d2) {
                    for (int i = 1; i <= N; i++) {
                        for (int j = 1; j <= N; j++) {
                            check[i][j] = 0;
                        }
                    }//초기화

                    for (int i = 0; i <= d1; i++) {
                        check[x + i][y - i] = 5;
                    }
                    for (int i = 0; i <= d2; i++) {
                        check[x + i][y + i] = 5;
                    }
                    for (int i = 0; i <= d2; i++) {
                        check[x + d1 + i][y - d1 + i] = 5;
                    }
                    for (int i = 0; i <= d1; i++) {
                        check[x + d2 + i][y + d2 - i] = 5;
                    }//경계선 다칠해주기


                    for (int i = x + 1; i < x + d1 + d2; i++) {
                        int cnt = 0;
                        for (int j = 1; j <= N; j++) {
                            if (check[i][j] == 5) {
                                if (cnt == 1) {
                                    cnt = 2;//두번째 경계선 만나면 cnt=2
                                }
                                if (cnt == 0) {
                                    cnt = 1;
                                }//첫번째 경계선 만나면 cnt=1
                            }
                            if (cnt == 1) {
                                check[i][j] = 5;//첫번째 경계선만난이후로 중간값 5
                            }
                        }
                    }//중간에 채워주기


                    for (int i = 1; i <= N; i++) {
                        for (int j = 1; j <= N; j++) {
                            if (check[i][j] != 5 && i >= 1 && i < x + d1 && 1 <= j && j <= y) {
                                check[i][j] = 1;
                            }
                            if (check[i][j] != 5 && i >= 1 && i <= x + d2 && y < j && j <= N) {
                                check[i][j] = 2;
                            }
                            if (check[i][j] != 5 && x + d1 <= i && i <= N && 1 <= j && j < y - d1 + d2) {
                                check[i][j] = 3;
                            }
                            if (check[i][j] != 5 && x + d2 < i && i <= N && y - d1 + d2 <= j && j <= N) {
                                check[i][j] = 4;
                            }//나머지 채우기
                        }
                    }

                    check1();
                }
            }
        }
    }
}


int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> map[i][j];
        }
    }

    solve();
    cout << answer;
}