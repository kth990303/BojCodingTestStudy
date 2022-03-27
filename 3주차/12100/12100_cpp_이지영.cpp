#include <iostream>
#include <algorithm>
using namespace std;

int N;
int board[21][21];
bool visit[21];
int maxx = 0;

void left() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 1; j <= N; j++) {
            if (!board[i][j]) {
                if (!tmp) { tmp = board[i][j]; continue; }
                //0이고 비교값 없을 때
                
                if (tmp == board[i][j]) {//비교값과 같을 때
                    for (int k = 1; k <= N; k++) {
                        if (visit[k] == false) {
                            board[i][k] = tmp * 2; visit[k] = true; tmp = 0; break;
                        }
                    }
                }
                else { //비교값과 같지않을 때 다음 값 비교값으로
                    for (int k = 1; k <= N; k++) {
                        if (visit[k] == false) {
                            board[i][k] = tmp; visit[k] = true; tmp = board[i][j]; break;
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//비교값과 합쳐질 자리가 없을 때 마지막에 비교값 넣어줌
            for (int k = 1; k <= N; k++) {
                if (visit[k] == false) {
                    board[i][k] = tmp; visit[k] = true; break;
                }
            }
        }
        //if (tmp != 0) {
        //    int* indexx = min_element(board[i], board[i] + 21);//방문하지 않은 가장 작은 index
        //    if (visit[*indexx] == false) {
        //        board[i][*indexx] = tmp; visit[*indexx] = true; break;
        //    }
        //} min element가 여러개 생겨서 오류 발생
 
        for (int k = 1; k <= N; k++) { //합쳐진 이후 이전 블록 0으로
            if (visit[k] == false) { board[i][k] =0;  }
        }
        memset(visit, false, sizeof(visit));
    }
}
void right() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = N; j >= 1; j--) {
            if (board[i][j] != 0) {
                if (tmp == 0) {
                    tmp = board[i][j];//0이고 비교값 없을 때
                }
                else {
                    if (tmp == board[i][j]) {//비교값과 같을 때
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[i][k] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //비교값과 같지않을 때 다음 값 비교값으로
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[i][k] = tmp; visit[k] = true; tmp = board[i][j]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//비교값과 합쳐질 자리가 없을 때 마지막에 비교값 넣어줌
            for (int k = N; k >= 1; k--) {
                if (visit[k] == false) {
                    board[i][k] = tmp; visit[k] = true; break;
                }
            }
        }
        
        for (int k = N; k >= 1; k--) { //합쳐진 이후 이전 블록 0으로
            if (visit[k] == false) { board[i][k] = 0; }
        }
        memset(visit, false, sizeof(visit));
    }
}
void up() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 1; j <= N; j++) {
            if (board[j][i] != 0) {
                if (tmp == 0) {
                    tmp = board[j][i];//0이고 비교값 없을 때
                }
                else {
                    if (tmp == board[j][i]) {//비교값과 같을 때
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[k][i] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //비교값과 같지않을 때 다음 값 비교값으로
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[k][i] = tmp; visit[k] = true; tmp = board[j][i]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//비교값과 합쳐질 자리가 없을 때 마지막에 비교값 넣어줌
            for (int k = 1; k <= N; k++) {
                if (visit[k] == false) {
                    board[k][i] = tmp; visit[k] = true; break;
                }
            }
        }
        for (int k = 1; k <= N; k++) { //합쳐진 이후 이전 블록 0으로
            if (visit[k] == false) { board[k][i] = 0; }
        }
        memset(visit, false, sizeof(visit));
    }
}
void down() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = N; j >= 1; j--) {
            if (board[j][i] != 0) {
                if (tmp == 0) {
                    tmp = board[j][i];//0이고 비교값 없을 때
                }
                else {
                    if (tmp == board[j][i]) {//비교값과 같을 때
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[k][i] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //비교값과 같지않을 때 다음 값 비교값으로
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[k][i] = tmp; visit[k] = true; tmp = board[j][i]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//비교값과 합쳐질 자리가 없을 때 마지막에 비교값 넣어줌
            for (int k = N; k >= 1; k--) {
                if (visit[k] == false) {
                    board[k][i] = tmp; visit[k] = true; break;
                }
            }
        }
        
        for (int k = N; k >= 1; k--) { //합쳐진 이후 이전 블록 0으로
            if (visit[k] == false) { board[k][i] = 0; }
        }
        memset(visit, false, sizeof(visit));
    }
}




void AtoA(int arr1[21][21], int arr2[21][21]) {
    for (int i = 1; i <= N; i++) {
        for (int j= 1; j <= N; j++) {
            arr1[i][j] = arr2[i][j];
        }
    }
}

void move(int cnt) {    
    if (cnt == 5) { //가장 큰 블럭
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (maxx < board[i][j]) {
                    maxx = board[i][j];
                    
                }
            }
        }
        return;//최대값 찾고 재귀 끝!
    }

    int M_temp[21][21] = { 0 };

    AtoA(M_temp, board);
    left(); move(cnt+1);    
    AtoA(board, M_temp);

    AtoA(M_temp, board);
    right(); move(cnt + 1);
    AtoA(board, M_temp);

    AtoA(M_temp, board);
    up(); move(cnt + 1);
    AtoA(board, M_temp);

    AtoA(M_temp, board);
    down(); move(cnt + 1);
    AtoA(board, M_temp);
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> board[i][j];
        }
    }
    move(0);
    
    /*for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cout << board[i][j]<<" ";
        }
        cout << "\n";
    }*/

    cout << maxx; exit(0);
}