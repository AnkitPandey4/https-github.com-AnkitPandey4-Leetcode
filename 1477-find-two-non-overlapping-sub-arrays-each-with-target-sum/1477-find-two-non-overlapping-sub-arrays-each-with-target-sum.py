class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        ans = float('inf')
        
        running_sum = 0
        l = 0
        
        for r in range(n):
            running_sum += arr[r]
            
            while running_sum > target:
                running_sum -= arr[l]
                l += 1
                
            if running_sum == target:
                current_len = r - l + 1
                if l > 0 and best[l - 1] != float('inf'):
                    ans = min(ans, best[l - 1] + current_len)
                
                best[r] = current_len
            
            if r > 0:
                best[r] = min(best[r], best[r - 1])
                
        return ans if ans != float('inf') else -1
