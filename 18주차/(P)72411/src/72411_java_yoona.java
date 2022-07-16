import java.util.*;

class Solution {
    HashMap<String, Integer> menu_set=new HashMap<>();
    TreeSet answer=new TreeSet<String>();
    public String[] solution(String[] orders, int[] course) {
        for(int i=0; i<orders.length; i++){ //주문 목록에서 최소 2가지 이상의 모든 메뉴 조합들 구하기
            for(int j=0; j<orders[i].length(); j++){
                find_collection(orders[i], String.valueOf(orders[i].charAt(j)), j+1);
            }
        }
        Deque deque=new ArrayDeque<String>();
        make_course(course, deque); //코스 만들기
        return Arrays.copyOf(answer.toArray(), answer.size(), String[].class);
    }

    void find_collection(String ordered, String newMenus, int start){ //가능한 조합 찾기
        for(int i=start; i<ordered.length(); i++){
            char[] addMenus_ch=(newMenus+ordered.charAt(i)).toCharArray();
            Arrays.sort(addMenus_ch);
            String addMenus=new String(addMenus_ch);
            Integer prev=menu_set.put(addMenus,1);
            if(prev!=null){ //이미 존재하는 조합 -> +1
                menu_set.put(addMenus,prev+1);
            }
            find_collection(ordered, addMenus, i+1);
        }
    }
    void make_course(int[] course, Deque deque){
        for(int i=0; i<course.length; i++){
            int max=2;
            for(Map.Entry<String, Integer> entry : menu_set.entrySet()){
                if(entry.getKey().length()==course[i]){
                    if(entry.getValue()>max){
                        deque.clear();
                        deque.addLast(entry.getKey());
                        max=entry.getValue();
                    }else if(entry.getValue()==max){
                        deque.addLast(entry.getKey());
                    }
                }
            }
            answer.addAll(deque);
            deque.clear();
        }
    }
}