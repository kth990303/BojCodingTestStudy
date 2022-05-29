import java.util.Arrays;

class Solution {
    String[] answer;
    public String[] solution(String[] files)
    {
        answer=new String[files.length];
        mergeSort(files,0,files.length-1);
        return answer;
    }
    void mergeSort(String[] files, int left, int right)
    {
        if(left==right) return;

        mergeSort(files,left,(left+right)/2);
        mergeSort(files,(left+right)/2+1,right);

        int mid=(left+right)/2;
        int firstIndex=left;
        int secondIndex=mid+1;
        int answerIndex=left;
        while(firstIndex<=mid && secondIndex<=right){
            if(checkPriority(files[firstIndex],files[secondIndex])){ //첫번째가 더 앞순위
                answer[answerIndex++]=files[firstIndex++];
            }else{ //두번쩨가 더 앞순위
                answer[answerIndex++]=files[secondIndex++];
            }
        }
        if(firstIndex>mid){
            while(answerIndex<=right){
                answer[answerIndex++]=files[secondIndex++];
            }
        }else if(secondIndex>right){
            while(answerIndex<=right){
                answer[answerIndex++]=files[firstIndex++];
            }
        }
        for(int i=left;i<=right;i++){
            files[i]=answer[i];
        }
    }
    boolean checkPriority(String first, String second)
    {
        String delimiter="\\d";
        String[] firstArr=first.split(delimiter);
        String[] secondArr=second.split(delimiter);
        int priority=firstArr[0].toLowerCase().compareTo(secondArr[0].toLowerCase());
        if(priority<0){ //first가 순서가 더 빠름
            return true;
        }else if(priority>0){ //second가 순서가 더 빠름
            return false;
        }else { //Head가 같을때
            delimiter="\\D+";
            firstArr=first.split(delimiter);
            secondArr=second.split(delimiter);
            int firstNum=Integer.parseInt(firstArr[1]);
            int secondNum=Integer.parseInt(secondArr[1]);
            if(firstNum<=secondNum){
                return true;
            }else{
                return false;
            }
        }
    }
}