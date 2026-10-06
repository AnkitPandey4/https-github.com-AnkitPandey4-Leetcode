class Solution:

  def minAddToMakeValid(self, s: str) -> int:
    l = 0  # unmatched '('
    r = 0  # unmatched ')'
    for c in s:
      if c == '(':
        l += 1
      else:
        if l == 0:
          r += 1
        else:
          l -= 1
    return l + r
