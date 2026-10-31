class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest,i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                if curr_end >= len(nums) - 1:
                    break
        return jumps            






        #dp = [float('inf')] *len(nums)
        #dp[0] = 0
        #for i in range(len(nums)):
         #   for j in range(1,nums[i] +1):
          #      if i+j < len(nums):
           #         dp[i+j]= min(dp[i+j],dp[i]+1)
        