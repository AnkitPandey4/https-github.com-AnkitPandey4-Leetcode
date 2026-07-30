from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        d = {}
        m = float("inf")
        
        # 1. Fixed variable name from 'list[i]' to 'list1[i]'
        for i in range(len(list1)):
            d[list1[i]] = i
            
        for j in range(len(list2)):
            if list2[j] in d:
                s = j + d[list2[j]]
                
                # 2. Corrected logic to clear results and update minimum
                if s < m:
                    m = s
                    res = [list2[j]]  # Reset list with the new minimum
                # 3. Changed to 'elif' to avoid duplicating elements
                elif s == m:
                    res.append(list2[j])
                    
        return res
