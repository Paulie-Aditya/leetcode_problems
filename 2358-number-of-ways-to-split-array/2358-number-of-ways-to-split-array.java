class Solution {
    public int waysToSplitArray(int[] nums) {
        int ways = 0;
        long left_sum = 0;
        long right_sum = 0;
        int n = nums.length;

        for(int i = 0; i<n;i++){
            right_sum += nums[i];
        }
        
        for(int i = 0; i<n-1;i++){
            right_sum-=nums[i];
            left_sum+= nums[i];
            if(left_sum >= right_sum){
                ways++;
            }
        }

        return ways;
    }
}