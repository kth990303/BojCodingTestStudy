import java.util.*;

class Solution {
    public int solution(int m, int n, String[] board) {
        int answer=0;
        boolean re=false;
        while(re=travel(m, n, board)){
            Stack<String> stack=new Stack<>();
            for(int j=0; j<n; j++){
                for(int i=0; i<m; i++){
                    if(Character.isUpperCase(board[i].charAt(j))){
                        stack.push(String.valueOf(board[i].charAt(j)));
                    }else if(Character.isLowerCase(board[i].charAt(j))){
                        answer++;
                    }
                }
                //보드 재정렬
                for(int i=m-1; i>=0; i--){
                    if(stack.empty()){
                        board[i]=board[i].substring(0,j)+"0"+board[i].substring(j+1); //빈 칸 -> "0"
                    }else{
                        board[i]=board[i].substring(0,j)+stack.pop()+board[i].substring(j+1);
                    }
                }
            }
        }
        return answer;
    }

    boolean travel(int m, int n, String[] board){
        boolean flag=false;
        for(int i=m-1; i>0; i--){ //ㄱ부분은 탐색 x
            for(int j=0; j<n-1; j++){
                char current=Character.toUpperCase(board[i].charAt(j));
                if(current=='0') {
                    continue;
                }
                char check=Character.toUpperCase(board[i-1].charAt(j));
                if(check!=current) {
                    continue;
                }
                check=Character.toUpperCase(board[i].charAt(j+1));
                if(check!=current){
                    continue;
                }
                check=Character.toUpperCase(board[i-1].charAt(j+1));
                if(check!=current){
                    j+=2;
                    continue;
                }
                char current_lower=Character.toLowerCase(current);
                board[i]=board[i].substring(0,j)+current_lower+current_lower+board[i].substring(j+2);
                board[i-1]=board[i-1].substring(0,j)+current_lower+current_lower+board[i-1].substring(j+2);
                flag=true;
            }
        }
        return flag;
    }
}