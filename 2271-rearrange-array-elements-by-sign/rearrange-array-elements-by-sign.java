class Solution {
    public int[] rearrangeArray(int[] nums) {
      ArrayList<Integer> a=new ArrayList<>();
      ArrayList<Integer> b=new ArrayList<>();
      for(int i:nums){
        if(i>=0){
            a.add(i);
        }
        else{
            b.add(i);
        }
      } 
      int j=0;
      for(int i=0;i<=nums.length-1;i++,j++){
            nums[i]=a.get(j);
            i++;
            nums[i]=b.get(j);
      } 
    return nums;
    }
}