class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();

        int maxRight = arr[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            int current = arr[i];

            arr[i] = maxRight;

            maxRight = max(maxRight, current);
        }

        arr[n - 1] = -1;

        return arr;
    }
};