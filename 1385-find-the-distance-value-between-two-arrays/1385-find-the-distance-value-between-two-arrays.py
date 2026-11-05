class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            ok = True 
            for y in arr2:
                if abs(x-y) <= d:
                    ok = False
                    break
            if ok:
                count += 1
        return count                
        