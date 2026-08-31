class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int minDistance = INT_MAX;
        int firstIndex = -1;
        int prevIndex = -1;
        int index = 1;
        
        ListNode* prev = head;
        ListNode* curr = head->next;
        
        while (curr->next != nullptr) {
            bool isMaxima = (curr->val > prev->val && curr->val > curr->next->val);
            bool isMinima = (curr->val < prev->val && curr->val < curr->next->val);
            
            if (isMaxima || isMinima) {
                if (firstIndex == -1) {
                    firstIndex = index;
                } else {
                    minDistance = min(minDistance, index - prevIndex);
                }
                prevIndex = index;
            }
            
            prev = curr;
            curr = curr->next;
            index++;
        }
        
        if (minDistance == INT_MAX) {
            return {-1, -1};
        }
        
        return {minDistance, prevIndex - firstIndex};
    }
};
