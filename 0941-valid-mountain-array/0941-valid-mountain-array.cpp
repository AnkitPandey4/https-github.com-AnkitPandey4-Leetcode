class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();

        int i = 0;
        int j = n - 1;

        // Increasing part
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }

        // Decreasing part
        while (j > 0 && arr[j - 1] > arr[j]) {
            j--;
        }

        // Both pointers must meet at the peak
        // Peak cannot be first or last element
        return i == j && i != 0 && i != n - 1;
    }
};