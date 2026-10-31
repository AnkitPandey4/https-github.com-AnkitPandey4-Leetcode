class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m ,n = len(s) , len(p)
        i=j=0
        star = -1
        match = 0
        while i < m:
            if j<n and (p[j]==s[i] or p[j]=='?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                star = j
                match = i 
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else :
                return False
        while j < n and p[j] == '*':
            j+=1
        return j == n                












       # s_idx = p_idx = 0
        #star_idx = -1
        #s_tmp = 0

        #while s_idx < len(s):
         #   if p_idx < len(p) and (p[p_idx] == 'q' or p[p_idx] == s[s_idx]):
          #      s_idx += 1
           #     p_idx += 1
            #elif p_idx < len(p) and p[p_idx] == '*':
             #   star_idx = p_idx
              #  s_tmp = s_idx
               # p_idx += 1
           # elif star_idx != -1:
            #    p_idx = star_idx +1
             #   s_tmp += 1
              #  s_idx = s_tmp
           # else:
            #    return False

       # while p_idx < len(p) and p[p_idx] == '*':
        #    p_idx += 1
        #return p_idx == len(p)        

                        
        