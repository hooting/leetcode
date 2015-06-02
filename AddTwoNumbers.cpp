/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == NULL){
            return l2;
        }
        if(l2 == NULL){
            return l1;
        }
        int carryBit = (l1->val + l2->val) / 10;
        ListNode* head = new ListNode((l1->val + l2->val) % 10);
        ListNode* prePivot = head;
        ListNode* pivot = NULL;
        ListNode* l1Pivot = l1->next;
        ListNode* l2Pivot = l2->next;
        while(l1Pivot != NULL && l2Pivot != NULL){
            int sum = l1Pivot->val + l2Pivot->val + carryBit;
            carryBit = sum / 10;
            pivot = new ListNode(sum % 10);
            prePivot->next = pivot;
            prePivot = pivot;
            l1Pivot = l1Pivot->next;
            l2Pivot = l2Pivot->next;
        }
        l1Pivot = l1Pivot == NULL ? l2Pivot : l1Pivot;
        while(l1Pivot != NULL){
            int sum = l1Pivot->val + carryBit;
            carryBit = sum / 10;
            pivot = new ListNode(sum % 10);
            prePivot->next = pivot;
            prePivot = pivot;
            l1Pivot = l1Pivot->next;
        }
        if(carryBit > 0){
            pivot = new ListNode(carryBit);
            prePivot->next = pivot;
        }
        return head;
        
    }
};