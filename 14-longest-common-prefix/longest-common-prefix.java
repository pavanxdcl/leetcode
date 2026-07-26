class Solution {
    public String longestCommonPrefix(String[] ar) {
        Arrays.sort(ar);
        char[] a=ar[0].toCharArray();
        char[] b=ar[ar.length-1].toCharArray();
        int i=0;
        String ans="";
        while(i<=Math.min(a.length-1,b.length-1) ) {
                if(a[i]==b[i]){
                    ans=ans+a[i];
                    i++;
                }
                else{
                    break;
                }
                
        }
        return ans;

    }
}