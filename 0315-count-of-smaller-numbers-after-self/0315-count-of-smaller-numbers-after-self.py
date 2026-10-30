class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(set(nums))
        rank = {v: i+1 for i,v in enumerate(sorted_nums)}
        n = len(rank)
        BIT = [0]*(n+2)

        def update(i):
            while i<= n:
                BIT[i] += 1
                i += i & -i
        def query(i):
            s=0
            while i>0:
                s += BIT[i]
                i -= i & -i 
            return s
        res = [0]*len(nums)
        for i in range(len(nums) -1,-1,-1):
            r = rank[nums[i]]
            res[i]= query(r-1)
            update(r)
        return res    
                           









        