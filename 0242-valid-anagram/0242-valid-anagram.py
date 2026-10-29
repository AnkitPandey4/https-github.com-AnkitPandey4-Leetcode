class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) != len(t):
         #   return false
        #from collections import counter
        #return counter(s) == counter(t)    
        #if len(s) != len(t):
         #   return false
          #  return false
        #from collections import counter
        #return counter(s) == counter(t)   

        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)     
        