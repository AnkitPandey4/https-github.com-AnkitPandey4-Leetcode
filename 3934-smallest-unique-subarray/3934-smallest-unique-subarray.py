from collections import Counter


class Solution:

    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        mod = (1 << 61) - 1
        base = 100003

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        for i, val in enumerate(nums):
            prefix[i + 1] = (prefix[i] * base + val) % mod
            power[i + 1] = (power[i] * base) % mod

        def has_unique_of_length(length: int) -> bool:
            counts = Counter()
            p = power[length]
            for start in range(n - length + 1):
                end = start + length
                h = (prefix[end] - prefix[start] * p) % mod
                counts[h] += 1
            return any(cnt == 1 for cnt in counts.values())

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                high = mid
            else:
                low = mid + 1

        return low
