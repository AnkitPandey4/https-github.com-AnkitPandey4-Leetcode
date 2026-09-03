/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int total_length = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            total_length++;
            curr = curr->next;
        }

        int base_size = total_length / k;
        int extra_nodes = total_length % k;

        vector<ListNode*> result(k, nullptr);
        curr = head;

        for (int i = 0; i < k && curr != nullptr; i++) {
            result[i] = curr;
            
            int current_part_size = base_size + (i < extra_nodes ? 1 : 0);

            for (int j = 1; j < current_part_size; j++) {
                curr = curr->next;
            }

            ListNode* next_part = curr->next;
            curr->next = nullptr;
            curr = next_part;
        }

        return result;
    }
};
