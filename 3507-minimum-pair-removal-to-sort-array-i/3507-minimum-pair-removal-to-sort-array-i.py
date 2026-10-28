class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        ops = 0

        def is_sorted(a):
            for i in range(1,len(a)):
                if a[i] < a[i-1]:
                    return False
            return True

        while not is_sorted(arr):
            min_sum = arr[0] + arr[1]
            idx = 0

            for i in range(1 , len(arr) - 1):
                s = arr[i] + arr[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            arr[idx]= min_sum
            arr.pop(idx + 1)
            ops += 1
        return ops                        

        