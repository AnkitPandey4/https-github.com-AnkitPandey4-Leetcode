class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0        






        #max_reach = 0
        #for i in range(len(nums)):
         #   if i > max_reach:
          #      return False
           # Max_reach=max(max_reach,i + nums[i])
           # if max_reach >= len(nums)-1:
            #    return True
        #return True            

        