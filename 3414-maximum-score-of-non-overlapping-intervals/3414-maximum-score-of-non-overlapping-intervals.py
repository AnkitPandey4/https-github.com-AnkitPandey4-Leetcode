from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # 1. Augment each interval with its original index: (left, right, weight, original_index)
        # Then sort by start time 'l'.
        A = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        n = len(A)
        
        # Extract sorted start times for binary searching the next valid non-overlapping interval
        starts = [item[0] for item in A]
        
        @lru_cache(None)
        def dp(i, count):
            # Base cases: no items left or no remaining choices allowed
            if i == n or count == 0:
                return (0, [])
            
            # --- Option 1: Skip the current interval ---
            max_w, best_indices = dp(i + 1, count)
            
            # --- Option 2: Take the current interval ---
            l, r, w, idx = A[i]
            # Find the first interval that starts strictly after the current interval ends
            next_idx = bisect_right(starts, r)
            
            take_w, take_indices = dp(next_idx, count - 1)
            new_w = w + take_w
            # Ensure the indices list remains sorted to satisfy lexicographical comparison requirements
            new_indices = sorted([idx] + take_indices)
            
            # --- Decision & Tie-Breaking ---
            if new_w > max_w:
                max_w, best_indices = new_w, new_indices
            elif new_w == max_w:
                # If weights match, choose the lexicographically smaller index configuration
                if not best_indices or new_indices < best_indices:
                    best_indices = new_indices
                    
            return (max_w, best_indices)
        
        # We can pick at most 4 intervals
        return dp(0, 4)[1]
