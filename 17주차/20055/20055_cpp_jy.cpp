#include<iostream>
#include<algorithm>
using namespace std;
struct belt{
    int num;
    int robot;
};
belt map[201], tmpp[201];
int cnt=0, N, K, x;
int main(){
    cin >> N >> K;
    for(int i=1; i<=2*N; i++){
        cin >> map[i].num;
        map[i].robot = 0;
    }
    int flag=1;
    while(true){
        //1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        tmpp[1] = map[2*N];
        for(int i=2; i<=2*N; i++) tmpp[i] = map[i-1];
        for(int i=1; i<=2*N; i++) map[i] = tmpp[i];
        if(map[N].robot) map[N].robot = 0;
        
        //2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        //로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        for(int i=N-1; i>=1; i--) {
            if(map[i].robot) {
                if(!map[i+1].robot && map[i+1].num >= 1) {
                    map[i+1].robot = map[i].robot;
                    map[i+1].num--;
                    if(map[i+1].num == 0) cnt++;
                    map[i].robot = 0;
                }
            }
        }
        if(map[N].robot) map[N].robot = 0;

        //3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if(map[1].num >= 1 && !map[1].robot) {
            map[1].robot = 1;
            map[1].num--;
            if(map[1].num == 0) cnt++;
        }

        //4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        if(cnt >= K) {
            cout << flag;
            return 0;
        }
        flag +=1;
    }
    return 0;
}
