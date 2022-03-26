#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int N, M, x, y, k; //����, ����, �ֻ��� ��ǥ, ��� ����
int map[21][21]; //����
int order[1001]; // ��ɰ�������
int dice[7]; //�ֻ��� 
int temp[7]; //��� ������ �迭

int dx[4] = { 0,0,-1,1 }; //���� �� �� �� ��
int dy[4] = { 1,-1,0,0 };

void solve(int n) {
    for (int i = 1; i <= 6; i++) {
        temp[i] = dice[i];
    }//temp �迭�� �ֻ��� ���� ����

    int nx = x + dx[n - 1];
    int ny = y + dy[n - 1];

    if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
        return;
    }//�ֻ����� �̵��ߴµ� �ٱ����� �̵��ҽ� ��� ����

    x = nx;
    y = ny; //�ֻ��� ��ǥ�� �̵�

    if (n == 1) {//�������� ��������
        dice[1] = temp[4];
        dice[2] = temp[2];
        dice[3] = temp[1];
        dice[4] = temp[6];
        dice[5] = temp[5];
        dice[6] = temp[3];
        if (map[x][y] == 0) { //�ֻ��� �ٴڿ� ���� 0�̸� �ֻ��� ���� �������̵�
            map[x][y] = dice[6];
            cout << dice[1] << "\n";
            return;
        }
        else {
            dice[6] = map[x][y]; //0�� �ƴѰ��� ĭ�� ���μ��� �ֻ��� �ٴ�����
            map[x][y] = 0; //�׸��� �ʿ��� 0����
            cout << dice[1] << "\n";
            return;
        }
    }
    if (n == 2) {//����
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
    if (n == 3) {//��������
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