class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sum_k = 0
        
        # Iterate through all possible divisors k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            possible = True
            prev_max = float('-inf')
            
            # Check each consecutive block of length k
            for i in range(0, n, k):
                current_min = float('inf')
                current_max = float('-inf')
                transitions = 0
                
                # Check internal cyclic monotonicity and retrieve min/max values
                for j in range(k):
                    curr = nums[i + j]
                    next_el = nums[i + (j + 1) % k] # Circular index rule
                    
                    if curr < current_min: current_min = curr
                    if curr > current_max: current_max = curr
                    
                    if next_el < curr:
                        transitions += 1
                        
                if transitions > 1 or current_min < prev_max:
                    possible = False
                    break
                    
                prev_max = current_max
                
            if possible:
                sum_k += k
                
        return sum_k
