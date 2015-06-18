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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* first = head;
        ListNode* second = NULL;
        ListNode* pre = NULL;
        head = head->next;
        do{
            second = first->next;
            first->next = second->next;
            second->next = first;
            if(pre != NULL){
                pre->next = second;
            }
            pre = first;
            first = first->next;
        }while(first != NULL && first->next != NULL);
        return head;
    }
};