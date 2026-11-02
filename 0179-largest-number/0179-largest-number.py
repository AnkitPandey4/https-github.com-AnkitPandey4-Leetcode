class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(x,y):
            if x + y> y + x:
                return -1
            elif x+y<y+x:
                return 1
            else:
                return 0
        nums = list(map(str,nums))
        nums.sort(key=cmp_to_key(cmp))
        if nums[0] == "0":
            return "0"
        return "".join(nums)                    
        