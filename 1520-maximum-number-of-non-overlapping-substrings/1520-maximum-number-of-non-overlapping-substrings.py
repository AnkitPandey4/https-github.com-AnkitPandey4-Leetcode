class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        left = [n] * 26
        right = [0] * 26
        
        # Record leftmost and rightmost indices
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = max(right[idx], i)
            
        intervals = []
        for i in range(n):
            ch = s[i]
            idx = ord(ch) - ord('a')
            if left[idx] != i:
                continue  # Not the start of the character's first occurrence
                
            # Try to extend the interval
            r = right[idx]
            valid = True
            j = i
            while j <= r:
                c_idx = ord(s[j]) - ord('a')
                if left[c_idx] < i:
                    valid = False
                    break
                r = max(r, right[c_idx])
                j += 1
                
            if valid:
                intervals.append((i, r))
                
        # Greedy interval scheduling (sort by end time)
        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
                
        return res
