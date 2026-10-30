class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        pref = [0]
        s = 0
        for x in nums:
            s += x
            pref.append(s)
        def sort_count(lo,hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort_count(lo , mid) + sort_count(mid, hi)
            #count = sort_count(lo , mid) + sort_count(mid,hi)
            j = k = mid
            for i in range(lo,mid):
                while k <hi and pref[k] - pref[i] < lower:
                    k += 1
                while j < hi and pref[j] - pref[i] <= upper:
                    j+=1
                count += j - k
            pref[lo:hi] = sorted(pref[lo:hi])
            return count
        return sort_count(0,len(pref))                

        