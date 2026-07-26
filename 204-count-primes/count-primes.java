class Solution {
    public int countPrimes(int n) {
        if(n<2){
            return 0;
        }
        int[] a=new int[n];
        a[0]=1;
        a[1]=1;
        for(int i=2;i<n;i++){
            for(int j=i+i;j<n;j=j+i){
                a[j]=1;
            }
        }
        int count=0;
        for(int i:a){
            if(i==0){
                count++;
            }
        }
        return count;
    }
}