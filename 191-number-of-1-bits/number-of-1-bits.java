class Solution {
    public int hammingWeight(int n) {
        int count=1;
        while(n>1){
            int r=n%2;
            if(r==1) {count++;}
            n=n/2;
        }   
        return count;
    }
}