import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        curr_max = float('-inf') 
        
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            curr_max = max(curr_max, lst[0])
            
        best_range = [-10**9, 10**9]
        
        while heap:
            curr_min, list_idx, elem_idx = heapq.heappop(heap)
            
            if curr_max - curr_min < best_range[1] - best_range[0]:
                best_range = [curr_min, curr_max]
                
            if elem_idx + 1 == len(nums[list_idx]):
                break
                
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            curr_max = max(curr_max, next_val)
            
        return best_range
