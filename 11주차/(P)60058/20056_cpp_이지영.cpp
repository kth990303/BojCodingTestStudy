#include <iostream>
//#include <cstring>
#include <algorithm>
#include <vector>
#include <limits.h>
#include<cstring>
using namespace std;

struct F
{
    int x;
    int y;
    int Massive;
    int Speed;
    int dir;
    //fireball 구조체
};

int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int td[] = { 0, 2, 4, 6 }; //모두 홀수이거나 짝수
int fd[] = { 1, 3, 5 ,7 };

int N, M, K;
vector<F> mapp[51][51];
vector<F> fireball;

void Move()
{
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            mapp[i][j].clear();
        }
    }

    for (int i = 0; i < fireball.size(); i++)
    {
        int x = fireball[i].x;
        int y = fireball[i].y;
        int Mass = fireball[i].Massive;
        int Speed = fireball[i].Speed;
        int dir = fireball[i].dir;

        int Move = Speed % N;
        int nx = x + dx[dir] * Move;
        int ny = y + dy[dir] * Move;
        if (nx > N) nx -= N;
        if (ny > N) ny -= N;
        if (nx < 1) nx += N;
        if (ny < 1) ny += N;
        mapp[nx][ny].push_back({ nx,ny,Mass,Speed,dir });
        fireball[i].x = nx;
        fireball[i].y = ny;
    }
    //1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다
}

void Sum()
{
    vector<F> Temp;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (mapp[i][j].size() == 0) { continue; }
            if (mapp[i][j].size() == 1)
            {
                Temp.push_back(mapp[i][j][0]);
                continue;
            }

            int Massive_Sum = 0;
            int Speed_Sum = 0;
            int Cnt = mapp[i][j].size();

            bool even = true;
            bool odd = true;
            for (int k = 0; k < mapp[i][j].size(); k++)
            {
                Massive_Sum += mapp[i][j][k].Massive;
                Speed_Sum += mapp[i][j][k].Speed;
                if (mapp[i][j][k].dir % 2 == 0) odd = false;
                else even = false;
            }

            int Mass = Massive_Sum / 5;
            int Speed = Speed_Sum / Cnt;
            if (Mass == 0) continue;
            if (even == true || odd == true)
            {
                for (int k = 0; k < 4; k++)    Temp.push_back({ i, j, Mass, Speed, td[k] });
            }
            else
            {
                for (int k = 0; k < 4; k++) Temp.push_back({ i, j, Mass, Speed, fd[k] });
            }
        }
        //2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
    }
    fireball = Temp;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    
    cin >> N >> M >> K;
    for (int i = 0; i < M; i++)
    {
        int r, c, m, s, d;
        cin >> r >> c >> m >> s >> d;
        fireball.push_back({ r, c, m, s, d });
        mapp[r][c].push_back({ r, c, m, s, d });
    }
    

    for (int i = 0; i < K; i++)
    {
        Move();
        Sum();
    }

    int Ans = 0;
    for (int i = 0; i < fireball.size(); i++) {
        Ans += fireball[i].Massive;
    }

    cout << Ans<<"\n";

    return 0;
}