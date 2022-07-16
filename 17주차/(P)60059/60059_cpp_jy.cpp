#include <vector>
using namespace std;

int N,M;
vector<vector<int>> map;

// 잠금이 해제되어있는지
bool check(vector<vector<int>>& key, int y, int x){
    bool ret = true;

    for(int i=y;i<y+M;i++)
        for(int j=x;j<x+M;j++)
            map[i][j]+=key[i-y][j-x];

    for(int i=M;i<M+N;i++){
        for(int j=M;j<M+N;j++){
            if(map[i][j]!=1){
                ret=false;
                break;
            }
        }
        if(!ret) break;
    }

    for(int i=y;i<y+M;i++)
        for(int j=x;j<x+M;j++)
            map[i][j]-=key[i-y][j-x];

    return ret;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    bool answer = false;

    M = key.size();
    N = lock.size();

    map = vector<vector<int>>(2*M+N,vector<int>(2*M+N));

    // 보드에 입력하기
    for(int i=M;i<M+N;i++)
        for(int j=M;j<M+N;j++)
            map[i][j]=lock[i-M][j-M];

    // 상하좌우 
    for(int i=0;i<N+M;i++){
        for(int j=0;j<N+M;j++){
            for(int k=0;k<4;k++){
                vector<vector<int>> tmp(M,vector<int>(M));
                for(int i=0;i<M;i++)
                    for(int j=0;j<M;j++)
                        tmp[i][j] = key[j][M-i-1];

                for(int i=0;i<M;i++)
                    for(int j=0;j<M;j++)
                        key[i][j] = tmp[i][j];

                if(check(key,i,j)){
                    answer = true;
                    break;
                }
            }
            if(answer) break;
        }
        if(answer) break;
    }

    return answer;
}