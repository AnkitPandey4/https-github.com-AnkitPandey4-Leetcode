class NumArray:

    def __init__(self, nums: list[int]):
        self.pref=[0]
        s = 0
        for x in nums:
            s += x
            self.pref.append(s)

            
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right + 1] - self.pref[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)