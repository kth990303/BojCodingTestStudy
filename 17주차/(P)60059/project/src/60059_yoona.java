class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        int n=lock.length;
        int m=key.length;
        int lock_empty=0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(lock[i][j]==0) lock_empty++;
            }
        }
        for(int i=0; i<4; i++){ //시계방향으로 4회전 체크
            if(match(lock, key, n, m, lock_empty)){
                return true;
            }
            key=rotate_key(key, key.length);
        }
        return false;
    }

    int[][] rotate_key(int[][] key, int n){
        int[][] newkey=new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                newkey[j][n-i-1]=key[i][j];
            }
        }
        return newkey;
    }

    boolean match(int[][] lock, int[][] key, int n, int m, int lock_empty){
        for(int i=0; i<m+n-1; i++){
            for(int j=0; j<m+n-1; j++){
                int k_row=m-i-1
               for(int r=m-i-1; r<m; r++){
                   for(int c=m-j-1; c<m; c++){
                       int l_row=m-c;
                       int l_col=
                   }
               }
            }
        }
    }
}