import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String,Integer> typeCount=new HashMap<String,Integer>();
        for(int i=0;i<clothes.length;i++){
            String getKey=clothes[i][1];
            if(typeCount.containsKey(getKey)){
                typeCount.replace(getKey,typeCount.get(getKey)+1);
            }else{
                typeCount.put(clothes[i][1],1);
            }
        }
        for(String key : typeCount.keySet()){
            answer=answer*(typeCount.get(key)+1);
        }
        return answer-1;
    }
}