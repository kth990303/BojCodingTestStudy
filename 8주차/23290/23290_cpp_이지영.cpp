#include <iostream>
//#include <cstring>
#include <algorithm>
#include <vector>
#include <limits.h>
#include<cstring>
using namespace std;

int M, S;
int sy, sx, eat_m = 0;
int smell[5][5];
bool visitt[5][5];
pair<int, int> path[3], tmpP[3];
int fdy[] = { 0, -1, -1, -1, 0, 1, 1, 1 }; //0-index
int fdx[] = { -1, -1, 0, 1, 1, 1, 0, -1 }; //0-index
int sdy[] = { -1, 0, 1, 0 }; 
int sdx[] = { 0, -1, 0, 1 };
vector<int> mapp[5][5], copyM[5][5];


void Fish() { 
	vector<int> tmpM[5][5]; // 이동 후를 담을 vector
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++) {
			if (mapp[i][j].size() == 0) { continue; } //물고기 존재 x 칸
			for (int k = 0; k < mapp[i][j].size(); k++) {
				int dir = mapp[i][j][k];
				int nd = dir; //이동 후 방향 담을 변수
				bool m = false; //이동 성공하면 true
				for (int d = 0; d < 8; d++) {
					int ny = i + fdy[nd];
					int nx = j + fdx[nd];
					nd--; if (nd < 0) nd = 7; // 반시계 방향
					if (ny < 1 || ny >4 || nx < 1 || nx>4) { continue; } // 범위 밖
					if (smell[ny][nx] > 0 || ny == sy && nx == sx) { continue; } // 물고기의 냄새 || 상어가 있음
					m = true;
					nd++; if (nd > 7) nd = 0; //회전한 것 취소
					tmpM[ny][nx].push_back(nd);
					break;
				}
				if (!m) tmpM[i][j].push_back(dir);
			}
		}
	}
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++)
			mapp[i][j] = tmpM[i][j];
	}
}

void paths(int y, int x, int cnt, int eat) { 
	if (cnt == 0) {
		memset(visitt, false, sizeof(visitt));
		eat_m = INT_MIN;
	}else if (cnt == 3) {
		if (eat_m < eat) {
			eat_m = eat;
			for (int i = 0; i < 3; i++) path[i] = tmpP[i];
		} //백트래킹으로 찾은 이동경로 업로드
		return;
	}
	for (int d = 0; d < 4; d++) {
		int ny = y + sdy[d];
		int nx = x + sdx[d];
		if (ny < 1 || ny >4 || nx < 1 || nx>4) { continue; }
		tmpP[cnt] = { ny, nx };
		if (visitt[ny][nx]) { 
			paths(ny, nx, cnt + 1, eat); 
		}else {
			visitt[ny][nx] = true;
			paths(ny, nx, cnt + 1, eat + mapp[ny][nx].size());
			visitt[ny][nx] = false;
		}
	}
}

void Shark() { 
	paths(sy, sx, 0, 0); 
	for (int i = 0; i < 3; i++) {
		sy = path[i].first;
		sx = path[i].second;
		if (mapp[sy][sx].size() == 0) { continue; }
		mapp[sy][sx].clear(); // 잡아먹기
		smell[sy][sx] = 3; // 냄새
	}
}

void r_Smell() { //냄새 없애기 (1턴)
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++) {
			if (smell[i][j] > 0) smell[i][j]--;
		}
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> M >> S;
	int fy, fx, fd;
	for (int i = 0; i < M; i++) { 
		cin >> fy >> fx >> fd;
		mapp[fy][fx].push_back(fd - 1);
	}
	cin >> sy >> sx;

	while (S--) {
		//1번 과정
		for (int i = 1; i < 5; i++) {
			for (int j = 1; j < 5; j++)
				copyM[i][j] = mapp[i][j];
		}
		Fish(); //2번 과정
		Shark(); //3번 과정
		r_Smell(); //4번 과정
		//5번 과정
		for (int i = 1; i < 5; i++) {
			for (int j = 1; j < 5; j++) {
				for (int k = 0; k < copyM[i][j].size(); k++)
					mapp[i][j].push_back(copyM[i][j][k]);
			}
		}
	}

	int Ans = 0;
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 5; j++) Ans += mapp[i][j].size();
	}
	cout<<Ans;
	//S번 끝난 후 물기고 총 수

	return 0;
}