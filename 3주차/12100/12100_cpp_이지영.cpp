#include <iostream>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int N;
int board[21][21];
bool visit[21];
int maxx = 0;

void init_visit() {
    for (int k = 1; k <= N; k++) {
        visit[k] = false;
    }
}
void left() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 1; j <= N; j++) {
            if (board[i][j] != 0 ) {
                if(tmp == 0){tmp = board[i][j];//0�̰� �񱳰� ���� ��
                }
                else {
                    if (tmp == board[i][j]) {//�񱳰��� ���� ��
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[i][k] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //�񱳰��� �������� �� ���� �� �񱳰�����
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[i][k] = tmp; visit[k] = true; tmp = board[i][j]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//�񱳰��� ������ �ڸ��� ���� �� �������� �񱳰� �־���
            for (int k = 1; k <= N; k++) {
                if (visit[k] == false) {
                    board[i][k] = tmp; visit[k] = true; break;
                }
            }
        }
        for (int k = 1; k <= N; k++) { //������ ���� ���� ��� 0����
            if (visit[k] == false) { board[i][k] =0;  }
        }
        init_visit();
    }
}
void right() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = N; j >= 1; j--) {
            if (board[i][j] != 0) {
                if (tmp == 0) {
                    tmp = board[i][j];//0�̰� �񱳰� ���� ��
                }
                else {
                    if (tmp == board[i][j]) {//�񱳰��� ���� ��
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[i][k] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //�񱳰��� �������� �� ���� �� �񱳰�����
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[i][k] = tmp; visit[k] = true; tmp = board[i][j]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//�񱳰��� ������ �ڸ��� ���� �� �������� �񱳰� �־���
            for (int k = N; k >= 1; k--) {
                if (visit[k] == false) {
                    board[i][k] = tmp; visit[k] = true; break;
                }
            }
        }
        for (int k = N; k >= 1; k--) { //������ ���� ���� ��� 0����
            if (visit[k] == false) { board[i][k] = 0; }
        }
        init_visit();
    }
}
void up() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 1; j <= N; j++) {
            if (board[j][i] != 0) {
                if (tmp == 0) {
                    tmp = board[j][i];//0�̰� �񱳰� ���� ��
                }
                else {
                    if (tmp == board[j][i]) {//�񱳰��� ���� ��
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[k][i] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //�񱳰��� �������� �� ���� �� �񱳰�����
                        for (int k = 1; k <= N; k++) {
                            if (visit[k] == false) {
                                board[k][i] = tmp; visit[k] = true; tmp = board[j][i]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//�񱳰��� ������ �ڸ��� ���� �� �������� �񱳰� �־���
            for (int k = 1; k <= N; k++) {
                if (visit[k] == false) {
                    board[k][i] = tmp; visit[k] = true; break;
                }
            }
        }
        for (int k = 1; k <= N; k++) { //������ ���� ���� ��� 0����
            if (visit[k] == false) { board[k][i] = 0; }
        }
        init_visit();
    }
}
void down() {
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = N; j >= 1; j--) {
            if (board[j][i] != 0) {
                if (tmp == 0) {
                    tmp = board[j][i];//0�̰� �񱳰� ���� ��
                }
                else {
                    if (tmp == board[j][i]) {//�񱳰��� ���� ��
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[k][i] = tmp * 2; visit[k] = true; tmp = 0; break;
                            }
                        }
                    }
                    else { //�񱳰��� �������� �� ���� �� �񱳰�����
                        for (int k = N; k >= 1; k--) {
                            if (visit[k] == false) {
                                board[k][i] = tmp; visit[k] = true; tmp = board[j][i]; break;
                            }
                        }
                    }
                }
            }
        }
        if (tmp != 0) {//�񱳰��� ������ �ڸ��� ���� �� �������� �񱳰� �־���
            for (int k = N; k >= 1; k--) {
                if (visit[k] == false) {
                    board[k][i] = tmp; visit[k] = true; break;
                }
            }
        }
        for (int k = N; k >= 1; k--) { //������ ���� ���� ��� 0����
            if (visit[k] == false) { board[k][i] = 0; }
        }
        init_visit();
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
    if (cnt == 5) { //���� ū ��
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (maxx < board[i][j]) {
                    maxx = board[i][j];
                }
            }
        }
        return;//�ִ밪 ã�� ��� ��!
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
    //left();
    /*for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cout << board[i][j]<<" ";
        }
        cout << "\n";
    }*/
    cout << maxx;

    return 0;
}