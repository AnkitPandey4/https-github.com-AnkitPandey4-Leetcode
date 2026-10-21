#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
private:
    const int kMod = 1e9 + 7;
    
    // Arrays representing tree nodes. Allocating 4 * n memory space.
    vector<long long> sum;
    vector<long long> sqSum;
    vector<long long> lazy;

    // Push lazy propagation down to children nodes
    void pushDown(int node, int l, int r, int mid) {
        if (lazy[node] == 0) return;
        
        long long val = lazy[node];
        
        // Update left child
        int leftLen = mid - l + 1;
        sqSum[2 * node] = (sqSum[2 * node] + 2 * val * sum[2 * node] + val * val % kMod * leftLen) % kMod;
        sum[2 * node] = (sum[2 * node] + val * leftLen) % kMod;
        lazy[2 * node] = (lazy[2 * node] + val) % kMod;
        
        // Update right child
        int rightLen = r - mid;
        sqSum[2 * node + 1] = (sqSum[2 * node + 1] + 2 * val * sum[2 * node + 1] + val * val % kMod * rightLen) % kMod;
        sum[2 * node + 1] = (sum[2 * node + 1] + val * rightLen) % kMod;
        lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % kMod;
        
        lazy[node] = 0;
    }

    // Update range [ql, qr] by adding 1
    void update(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            long long len = r - l + 1;
            sqSum[node] = (sqSum[node] + 2 * sum[node] + len) % kMod;
            sum[node] = (sum[node] + len) % kMod;
            lazy[node] = (lazy[node] + 1) % kMod;
            return;
        }
        
        int mid = l + (r - l) / 2;
        pushDown(node, l, r, mid);
        
        if (ql <= mid) update(2 * node, l, mid, ql, qr);
        if (qr > mid) update(2 * node + 1, mid + 1, r, ql, qr);
        
        sum[node] = (sum[2 * node] + sum[2 * node + 1]) % kMod;
        sqSum[node] = (sqSum[2 * node] + sqSum[2 * node + 1]) % kMod;
    }

public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        
        sum.assign(4 * n, 0);
        sqSum.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        
        unordered_map<int, int> lastSeen;
        long long totalAns = 0;
        
        for (int r = 0; r < n; ++r) {
            // If the number was seen before, distinct count only increases after its last position
            int l = lastSeen.count(nums[r]) ? lastSeen[nums[r]] + 1 : 0;
            
            // Add 1 to the distinct counts of all subarrays starting from l to r
            update(1, 0, n - 1, l, r);
            
            lastSeen[nums[r]] = r;
            
            // The root of the tree (sqSum[1]) holds the sum of squares of all active subarrays
            totalAns = (totalAns + sqSum[1]) % kMod;
        }
        
        return totalAns;
    }
};
