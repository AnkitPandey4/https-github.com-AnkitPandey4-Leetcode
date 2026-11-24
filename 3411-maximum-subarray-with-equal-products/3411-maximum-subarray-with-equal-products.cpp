#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    int maxLength(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int mx = 0;
        long long ml = 1;
        for (int x : nums) {
            mx = max(mx, x);
            ml = lcm(ml, static_cast<long long>(x));
        }
        long long maxProd = ml * mx;

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long prod = 1;
            long long g = 0;
            long long l = 1;
            for (int j = i; j < n; ++j) {
                long long val = nums[j];
                prod *= val;
                g = gcd(g, val);
                l = lcm(l, val);

                if (prod == g * l) {
                    ans = max(ans, j - i + 1);
                }
                if (prod > maxProd) {
                    break;
                }
            }
        }
        return ans;
    }
};
