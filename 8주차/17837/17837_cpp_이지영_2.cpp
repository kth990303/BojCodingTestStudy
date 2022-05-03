#include <iostream>
//#include <cstring>
#include <algorithm>
#include <vector>
#include <limits.h>
using namespace std;

struct mal
{
	int x, y, d;
}m[11];//말의 구조체
int N, K;
int dx[5] = { 0, 1, -1, 0, 0 };
int dy[5] = { 0, 0, 0, -1, 1 };
int map[14][14];
int rev[5] = { 0, 2, 1, 4, 3 };//방향 반대로 갈때
vector<int> marray[14][14];

int move(int i)
{
	int ny = m[i].y + dy[m[i].d];
	int nx = m[i].x + dx[m[i].d];
	if (ny > N || nx > N || nx <1 || ny <1 || map[ny][nx] == 2)
	{
		m[i].d = rev[m[i].d];//방향 반대로
		ny = m[i].y + dy[m[i].d];
		nx = m[i].x + dx[m[i].d];
		if (ny > N || nx > N || nx <1 || ny <1 || map[ny][nx] == 2)
			return 0;
		//칸 벗어나거나 파란색일때
	}
	vector<int>& curr = marray[m[i].y][m[i].x]; //현재 칸의 말들
	vector<int>& next = marray[ny][nx]; //이동한 칸에 있는 말들

	auto it = find(curr.begin(), curr.end(), i);

	if (map[ny][nx] == 1)
		reverse(it, curr.end()); //빨간색일때 순서 반대로
	for (auto t = it; t != curr.end(); t++)
	{
		m[*t].x = nx;
		m[*t].y = ny;
		next.push_back(*t); //이동
	}
	curr.erase(it, curr.end()); //이동 완료한 말들 지워줌
	return (next.size()); //턴 완료하고 쌓인 말의 개수 리턴
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

	cin >> N >> K;
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			cin >> map[i][j];
	for (int j = 1; j <= K; j++)
	{
		cin >> m[j].y >> m[j].x >> m[j].d;
		marray[m[j].y][m[j].x].push_back(j);//위치에 몇번 말 있는지 저장
	}

	int turn = 0;
	while(turn<=1000){
		turn += 1;
		for (int k = 1; k <= K; k++)
		{
			if (move(k) >= 4)
			{ 
				cout << turn << "\n";
				return 0;
				//말이 네개 쌓이는 경우
			}
		}
	}
	
	cout << "-1";
	//턴의 번호가 1000보다 크거나 게임이 종료되지 않는 경우

    return 0;
}