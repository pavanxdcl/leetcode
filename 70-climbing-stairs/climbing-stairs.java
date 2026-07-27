class Solution {
    public int climbStairs(int n) {
        
        if(n==0){
        return 0;}
        if(n==1){
        return 1;
        }
        if(n==2){
            return 2;
        }
        
        int[] a=new int[n];
        a[0]=1;
        a[1]=2;
        for(int i=2;i<=n-1;i++){
            a[i]=a[i-1]+a[i-2];
        }
        return a[a.length-1];
    }
}