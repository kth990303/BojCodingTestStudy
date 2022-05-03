#include <iostream>
//#include <cstring>
#include <algorithm>
#include <vector>
#include <limits.h>
using namespace std;

struct mal
{
	int x, y, d;
}m[11];//���� ����ü
int N, K;
int dx[5] = { 0, 1, -1, 0, 0 };
int dy[5] = { 0, 0, 0, -1, 1 };
int map[14][14];
int rev[5] = { 0, 2, 1, 4, 3 };//���� �ݴ�� ����
vector<int> marray[14][14];

int move(int i)
{
	int ny = m[i].y + dy[m[i].d];
	int nx = m[i].x + dx[m[i].d];
	if (ny > N || nx > N || nx <1 || ny <1 || map[ny][nx] == 2)
	{
		m[i].d = rev[m[i].d];//���� �ݴ��
		ny = m[i].y + dy[m[i].d];
		nx = m[i].x + dx[m[i].d];
		if (ny > N || nx > N || nx <1 || ny <1 || map[ny][nx] == 2)
			return 0;
		//ĭ ����ų� �Ķ����϶�
	}
	vector<int>& curr = marray[m[i].y][m[i].x]; //���� ĭ�� ����
	vector<int>& next = marray[ny][nx]; //�̵��� ĭ�� �ִ� ����

	auto it = find(curr.begin(), curr.end(), i);

	if (map[ny][nx] == 1)
		reverse(it, curr.end()); //�������϶� ���� �ݴ��
	for (auto t = it; t != curr.end(); t++)
	{
		m[*t].x = nx;
		m[*t].y = ny;
		next.push_back(*t); //�̵�
	}
	curr.erase(it, curr.end()); //�̵� �Ϸ��� ���� ������
	return (next.size()); //�� �Ϸ��ϰ� ���� ���� ���� ����
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
		marray[m[j].y][m[j].x].push_back(j);//��ġ�� ��� �� �ִ��� ����
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
				//���� �װ� ���̴� ���
			}
		}
	}
	
	cout << "-1";
	//���� ��ȣ�� 1000���� ũ�ų� ������ ������� �ʴ� ���

    return 0;
}