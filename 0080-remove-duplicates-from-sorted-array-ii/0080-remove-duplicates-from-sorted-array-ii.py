class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 0
        for num in nums:
            if(cnt < 2 or num != nums[cnt -2]):
                nums[cnt]=num
                cnt += 1
        return cnt        





               

        