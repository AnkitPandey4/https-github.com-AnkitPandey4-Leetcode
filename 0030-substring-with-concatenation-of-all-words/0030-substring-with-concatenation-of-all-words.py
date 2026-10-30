from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            window = defaultdict(int)
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    window[word] += 1
                    count += 1
                    
                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    if count == num_words:
                        res.append(left)
                else:
                    window.clear()
                    count = 0
                    left = right
                    
        return res
