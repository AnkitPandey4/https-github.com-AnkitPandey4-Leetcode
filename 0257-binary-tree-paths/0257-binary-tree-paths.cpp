class Solution {
public:
    vector<string> ans;

    void dfs(TreeNode* node, string path) {
        if (node->left == nullptr && node->right == nullptr) {
            ans.push_back(path);
            return;
        }

        if (node->left != nullptr) {
            dfs(node->left, path + "->" + to_string(node->left->val));
        }

        if (node->right != nullptr) {
            dfs(node->right, path + "->" + to_string(node->right->val));
        }
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == nullptr) return {};

        string path = to_string(root->val);
        dfs(root, path);

        return ans;
    }
};