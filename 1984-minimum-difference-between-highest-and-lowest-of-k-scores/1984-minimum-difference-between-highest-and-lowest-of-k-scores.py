class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        nums.sort()
        ans = float('inf')
        #ans = float('inf')
        #for i in range(len(nums)  - k + 1):

        for i in range(len(nums)- k + 1):

            ans = min(ans,nums[i + k -1] - nums[i])
            #ans = min(ans, nums[i+ k -1] - nums[i])

        return ans    
        