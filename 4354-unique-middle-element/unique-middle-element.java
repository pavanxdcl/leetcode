class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int i=0;
        int j=nums.length-1;
        while(i<j){
            if(nums[i]==nums[nums.length/2] || nums[j]==nums[nums.length/2]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}