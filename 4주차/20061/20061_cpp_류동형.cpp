#include <iostream>
#include <algorithm>

using namespace std;
int red[4][4];
int blue[4][6];
int green[6][4];
int N;
int score = 0;
int count_block = 0;

int check_blue(int x, int y) { //몇번째 칸에 들어가야할지 확인하는 함수
    for (int i = 1; i <= 5; i++) {
        if (blue[x][i] == 1) {
            return i-1;
        }
    }
    return 5;
}

int check_green(int x, int y) { //몇번째 칸에 들어가야할지 확인하는 함수
    for (int i = 1; i <= 5; i++) {
        if (green[i][y] == 1) {
            return i-1;
        }
    }
    return 5;
}

void move_blue() {
    for (int i = 5; i >= 1; i--) {
        if (blue[0][i] == 1 && blue[1][i] == 1 && blue[2][i] == 1 && blue[3][i] == 1) {//한줄이 전부 차있으면
            score++;
            for (int j = i; j >= 1; j--) {//한줄씩이동
                blue[0][j] = blue[0][j - 1]; blue[1][j] = blue[1][j - 1]; blue[2][j] = blue[2][j - 1]; blue[3][j] = blue[3][j - 1];
            }i++;
            blue[0][0] = 0; blue[1][0] = 0; blue[2][0] = 0; blue[3][0] = 0;//마지막줄 채워주기
        }
    }

    int cnt1 = 0;
    int cnt2 = 0;
    for (int i = 0; i <= 3; i++) {
        if (blue[i][1] == 1) {
            cnt1++;
        }
        if (blue[i][0] == 1) {
            cnt2++;
        }
    }//연한칸의 색에 하나라도 있으면 한줄씩 밀어주기
    
    if (cnt1 > 0) {
        for (int i = 5; i >= 1; i--) {
            blue[0][i] = blue[0][i - 1]; blue[1][i] = blue[1][i - 1]; blue[2][i] = blue[2][i - 1]; blue[3][i] = blue[3][i - 1];
        }
        blue[0][0] = 0; blue[1][0] = 0; blue[2][0] = 0; blue[3][0] = 0;
    }
    if (cnt2 > 0) {
        for (int i = 5; i >= 1; i--) {
            blue[0][i] = blue[0][i - 1]; blue[1][i] = blue[1][i - 1]; blue[2][i] = blue[2][i - 1]; blue[3][i] = blue[3][i - 1];
        }
        blue[0][0] = 0; blue[1][0] = 0; blue[2][0] = 0; blue[3][0] = 0;
    }
}

void move_green() {
    for (int i = 5; i >= 1; i--) {
        if (green[i][0] == 1 && green[i][1] == 1 && green[i][2] == 1 && green[i][3] == 1) {//한줄이 전부 차있으면
            score++;
            for (int j = i; j >= 1; j--) {
                green[j][0] = green[j-1][0]; green[j][1] = green[j-1][1]; green[j][2] = green[j-1][2]; green[j][3] = green[j-1][3]; 
            }i++;
            green[0][0] = 0; green[0][1] = 0; green[0][2] = 0; green[0][3] = 0;
        }
    }

    int cnt1 = 0;
    int cnt2 = 0;
    for (int i = 0; i <= 3; i++) {
        if (green[1][i] == 1) {
            cnt1++;
        }
        if (green[0][i] == 1) {
            cnt2++;
        }
    }

    if (cnt1 > 0) {
        for (int i = 5; i >= 1; i--) {
            green[i][0] = green[i - 1][0]; green[i][1] = green[i - 1][1]; green[i][2] = green[i - 1][2]; green[i][3] = green[i - 1][3];
        }
        green[0][0] = 0; green[0][1] = 0; green[0][2] = 0; green[0][3] = 0;
    }
    if (cnt2 > 0) {
        for (int i = 5; i >= 1; i--) {
            green[i][0] = green[i - 1][0]; green[i][1] = green[i - 1][1]; green[i][2] = green[i - 1][2]; green[i][3] = green[i - 1][3];
        }
        green[0][0] = 0; green[0][1] = 0; green[0][2] = 0; green[0][3] = 0;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for (int i = 1; i <= N; i++) {
        int c, x, y;
        int blue_idx = 0;
        int green_idx = 0;
        cin >> c >> x >> y;
        if (c == 1) {
            blue_idx = check_blue(x, y);
            green_idx = check_green(x, y);
            blue[x][blue_idx] = 1;
            green[green_idx][y] = 1;
            move_blue();
            move_green();
        }
        else if(c == 2) {
            blue_idx = check_blue(x, y);
            green_idx = min(check_green(x, y), check_green(x, y + 1));
            blue[x][blue_idx] = 1;
            blue[x][blue_idx - 1] = 1;
            green[green_idx][y] = 1;
            green[green_idx][y + 1] = 1;
            move_blue();
            move_green();
        }
        else if (c == 3) {
            blue_idx = min(check_blue(x, y), check_blue(x + 1, y));
            green_idx = check_green(x, y);
            blue[x][blue_idx] = 1;
            blue[x + 1][blue_idx] = 1;
            green[green_idx][y] = 1;
            green[green_idx - 1][y] = 1;
            move_blue();
            move_green();
        }
    }

    for (int i = 0; i <= 3; i++) {
        for (int j = 0; j <= 5; j++) {
            if (blue[i][j] == 1) {
                count_block++;
            }
            if (green[j][i] == 1) {
                count_block++;
            }
        }
    }

    /*
    for (int i = 0; i <= 3; i++) {
        for (int j = 0; j <= 5; j++) {
            cout << blue[i][j] << " ";
        }cout << "\n";
    }

    for (int i = 0; i <= 5; i++) {
        for (int j = 0; j <= 3; j++) {
            cout << green[i][j] << " ";
        }cout << "\n";
    }*/

    cout << score << "\n";
    cout << count_block;
}