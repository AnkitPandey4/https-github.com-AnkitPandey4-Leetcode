class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min((x for x in nums1 if x & 1), default=None)
        
        if mn is None:
            return True
            
        return all(x > mn for x in nums1 if x % 2 == 0)
