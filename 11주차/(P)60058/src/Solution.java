public class Solution {
    public String solution(String p) {
        String answer = "1";
        char[] u=new char[p.length()];
        char[] v=new char[p.length()];
//        ()))((()
//        ()))((    ())(
//        ()    )(
//        ()
        int index=divide(p);

        return answer;
    }

    int divide(String p)
    {
        int open=0;
        int close=0;
        int index=0;
        for(index=0;i<p.length();i++){
            if(p.charAt(i)=='('){
                open++;
            }else{
                close--;
            }
            if(open==close) break;
        }
        return index;
    }
}
