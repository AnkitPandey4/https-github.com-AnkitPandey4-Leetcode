# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = head 
        l = 0 
        while arr: 
            l += 1 
            arr = arr.next  
        w = l // k 
        r = l % k 
        
        curr = head 
        res = [] 
        
        for i in range(k):
            taphead = curr  
            cw = w + (1 if r > 0 else 0)
            r -= 1
            
            prev = None
            for _ in range(cw):
                if curr:
                    prev = curr
                    curr = curr.next
            
            
            if prev:
                prev.next = None
                
            res.append(taphead)
            
        return res
