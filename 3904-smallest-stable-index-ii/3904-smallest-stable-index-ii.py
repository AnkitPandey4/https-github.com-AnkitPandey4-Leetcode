class Solution:

  def firstStableIndex(self, nums: list[int], k: int) -> int:
    n = len(nums)
    min_val = [float('inf')] * n
    min_val[-1] = nums[-1]

    # Build suffix minimum array
    for i in range(n - 2, -1, -1):
      min_val[i] = min(min_val[i + 1], nums[i])

    max_val = 0
    # Traverse and check instability score
    for i in range(n):
      max_val = max(max_val, nums[i])
      if max_val - min_val[i] <= k:
        return i

    return -1
