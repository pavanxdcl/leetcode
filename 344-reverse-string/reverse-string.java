class Solution {
    public void reverseString(char[] a) {
        int i=0;
        int j=a.length-1;
        while(i<j){
            char x=a[i];
            a[i]=a[j];
            a[j]=x;
            i=i+1;
            j--;
        }
        
    }
}