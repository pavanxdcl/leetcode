class Solution {
    public String largestOddNumber(String num) {
        String ans="";
        String temp="";
        for(char i:num.toCharArray()){
            temp=temp+i;
            if((i-48)%2==1){
                ans=temp;
            }
        }
        return ans;
    }
}