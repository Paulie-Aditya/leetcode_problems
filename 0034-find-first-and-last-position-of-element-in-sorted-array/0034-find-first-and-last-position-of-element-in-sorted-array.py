class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = []

        try:
            x.append(nums.index(target))
            x.append((len(nums)-1)-(nums[::-1].index(target)))
        except:
            x = [-1,-1]
            return x
        return x