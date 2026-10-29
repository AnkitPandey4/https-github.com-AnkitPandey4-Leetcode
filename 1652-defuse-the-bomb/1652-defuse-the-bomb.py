class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
            
        if k > 0:
            window = sum(code[1:k+1])
            for i in range(n):
                res[i] = window
                window = window - code[(i + 1) % n] + code[(i + k + 1) % n]
        else:
            k = -k  
            window = sum(code[n-k:])
            for i in range(n):
                res[i] = window
                window = window - code[(i - k) % n] + code[i % n]
                
        return res
