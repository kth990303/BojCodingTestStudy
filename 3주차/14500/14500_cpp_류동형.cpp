#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int N, M;//세로 가로
int map[501][501];
int answer = 0;
int arr[19][4][2] = {
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}}, //세로로 일자
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}}, //가로로 일자
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}}, 
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},
    {{0, 0}, {1, -2}, {1, -1}, {1, 0}},
    {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
    {{0, 0}, {1, 0}, {2, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {1, -1}, {1, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {1, 1}},
    {{0, 0}, {1, -1}, {1, 0}, {2, 0}},
};

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> map[i][j];
        }
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            int temp = 0;
            for (int k = 0; k < 19; k++) {
                int temp1 = 0; //회전시켜서 나올 수 있는 도형 19개를 다 넣어보기
                for (int l = 0; l < 4; l++) {
                    int dx = arr[k][l][0];
                    int dy = arr[k][l][1];
                    int x = i + dx;
                    int y = j + dy;
                    if (1 > x || x > N || 1 > y || y > M) { //도형의 한 픽셀이라도 범위 벗어나면 그 도형은 취소
                        temp1 = 0;
                        break;
                    }
                    temp1 += map[x][y]; //도형중 하나 값 픽셀 다 더하기
                }
                temp = max(temp, temp1); //i,j좌표에서 생성한 도형중 합이 가장 큰거
            }
            answer = max(temp, answer); //전체좌표에서 가장 큰거
        }
    }

    cout << answer;
}