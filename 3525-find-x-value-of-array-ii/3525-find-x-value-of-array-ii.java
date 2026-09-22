class Solution {

    static class Node {
        int product;
        int[] count;

        Node(int k) {
            count = new int[k];
        }
    }

    int k;
    Node[] tree;

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.k = k;

        int n = nums.length;
        tree = new Node[4 * n];

        build(nums, 1, 0, n - 1);

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {

            int index = queries[i][0];
            int value = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];

            // Permanent update
            update(1, 0, n - 1, index, value % k);

            // Query [start, n - 1]
            Node result = query(1, 0, n - 1, start, n - 1);

            ans[i] = result.count[x];
        }

        return ans;
    }

    // Build segment tree
    private void build(int[] nums, int node, int left, int right) {

        tree[node] = new Node(k);

        if (left == right) {

            int value = nums[left] % k;

            tree[node].product = value;

            // Only one non-empty prefix
            tree[node].count[value] = 1;

            return;
        }

        int mid = left + (right - left) / 2;

        build(nums, node * 2, left, mid);
        build(nums, node * 2 + 1, mid + 1, right);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    // Point update
    private void update(
            int node,
            int left,
            int right,
            int index,
            int value) {

        if (left == right) {

            tree[node].product = value;

            tree[node].count = new int[k];
            tree[node].count[value] = 1;

            return;
        }

        int mid = left + (right - left) / 2;

        if (index <= mid) {
            update(node * 2, left, mid, index, value);
        } else {
            update(node * 2 + 1, mid + 1, right, index, value);
        }

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    // Range query
    private Node query(
            int node,
            int left,
            int right,
            int ql,
            int qr) {

        // Completely inside
        if (ql <= left && right <= qr) {
            return tree[node];
        }

        int mid = left + (right - left) / 2;

        // Completely in left child
        if (qr <= mid) {
            return query(node * 2, left, mid, ql, qr);
        }

        // Completely in right child
        if (ql > mid) {
            return query(node * 2 + 1, mid + 1, right, ql, qr);
        }

        // Crosses both children
        Node leftNode =
                query(node * 2, left, mid, ql, qr);

        Node rightNode =
                query(node * 2 + 1, mid + 1, right, ql, qr);

        return merge(leftNode, rightNode);
    }

    // Merge two consecutive segments
    private Node merge(Node left, Node right) {

        Node result = new Node(k);

        /*
         * Product of the entire combined segment
         */
        result.product =
                (left.product * right.product) % k;

        /*
         * Prefixes completely inside left segment.
         */
        for (int r = 0; r < k; r++) {
            result.count[r] += left.count[r];
        }

        /*
         * Prefixes that:
         *
         * 1. contain the entire left segment
         * 2. then contain some non-empty prefix of right
         *
         * If right prefix has remainder r,
         * its new remainder becomes:
         *
         * left.product * r % k
         */
        for (int r = 0; r < k; r++) {

            int newRemainder =
                    (left.product * r) % k;

            result.count[newRemainder] +=
                    right.count[r];
        }

        return result;
    }
}