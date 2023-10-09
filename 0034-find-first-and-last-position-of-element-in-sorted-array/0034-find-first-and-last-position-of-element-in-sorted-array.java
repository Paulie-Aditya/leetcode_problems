class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int n = nums.length;
        int low = 0;
        int high = n - 1;
        int mid = 0;
        boolean flag = false;

        while(low<=high){
            mid = low+ (high-low)/2;
            if(nums[mid] == target){
                flag = true;
                break;
            }
            else if(nums[mid]>target){
                high = mid-1;
            }
            else if(nums[mid]<target){
                low = mid+1;
            }
        }

        if(flag){
            int temp = mid;
            int[] to_return  = new int[2];
            while(temp>=0 && nums[temp] == target){
                temp--;
            }
            temp++;
            to_return[0] = temp;
            temp = mid;
            while(temp<n && nums[temp] == target){
                temp++;
            }
            temp--;
            to_return[1] = temp;

            return to_return;

        }
        else{
            int[] to_return = new int[2];
            to_return[0] = -1;
            to_return[1] = -1;
            return to_return;
        }

        
    }
}