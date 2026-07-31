class Solution:
    def containsNearbyAlmostDuplicate(self , nums: List[int],k:int,t:int)->bool:

        window = SortedList()
        for i , num in enumerate(nums):
            pos = window.bisect_left(num - t)
            if pos < len(window) and window[pos] <= num + t:
                return True
            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])
        return False            

        