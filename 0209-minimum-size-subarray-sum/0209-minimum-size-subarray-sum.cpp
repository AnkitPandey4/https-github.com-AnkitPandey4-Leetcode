class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int n = nums.size();
        int min_len = INT_MAX;
        int left = 0;
        int current_sum = 0;

        // Expand right pointer
        for (int right = 0; right < n; ++right) {
            current_sum += nums[right];

            // Contract left pointer when sum meets/exceeds target
            while (current_sum >= target) {
                min_len = std::min(min_len, right - left + 1);
                current_sum -= nums[left++];
            }
        }

        return (min_len == INT_MAX) ? 0 : min_len;
    }
};