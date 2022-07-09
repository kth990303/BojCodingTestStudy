import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    int solution() throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int[][] conveyor=new int[n*2][2];   //num칸의 컨베이어 [0]:내구도 [1]:로봇유무(0/1)
        for(int i = 0; i<n*2;i++){
            conveyor[i][0]=Integer.parseInt(st.nextToken());
            conveyor[i][1]=0;
        }
        br.close();

        int count=1;
        while(true){
            int knum=auto_rotate(conveyor, n); //자동 회전
            if(knum>=k) return (count==1)?1:count-1; //내구도 0 >= k개 면 종료
            rotate(conveyor, n); //수동 이동
            if(conveyor[0][0]>0){ //내구도가 0 이상이면 로봇 올리기
                conveyor[0][0]--;
                conveyor[0][1]=1;
            }
            count++;
        }
    }
    int auto_rotate(int[][] conveyor, int n){
        int k=0;
        int[] prev={conveyor[0][0], conveyor[0][1]};
        for(int i = 1; i<2*n+1; i++){
            int[] tmp={conveyor[i%(2*n)][0],conveyor[i%(2*n)][1]};
            conveyor[i%(2*n)][0]=prev[0];
            conveyor[i%(2*n)][1]=prev[1];
            prev=tmp;
            k+=(conveyor[i%(2*n)][0]==0)?1:0;
        }
        conveyor[n-1][1]=0;//로봇 내리기
        return k;
    }
    void rotate(int[][] conveyor, int n){
        int prev=conveyor[0][1];
        for(int i=1; i<n; i++){
            if(prev==0){ //현재칸 full
                prev=conveyor[i][1];
            }else if(conveyor[i][1]==1) { //현재칸 full
                prev=1;
            }else if(conveyor[i][0]==0){ //내구도x
                prev=0;
            }else{ //로봇 수동 이동
                conveyor[i][0]--;
                conveyor[i][1]=prev;
                conveyor[i-1][1]=0;
                prev=0;
            }
        }
        conveyor[n-1][1]=0; //로봇 내리기
    }
}
