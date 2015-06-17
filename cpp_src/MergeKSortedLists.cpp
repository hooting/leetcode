/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /**
  * use min heap to store the ks elements from ks linked list
  * each time fetch a element from min heap cost O(lgK);
  * the total complexity is (knlgK).
  * Here,we assume each list length is n.
  */
class Solution {

struct comparator{
	bool operator() ( ListNode* i, ListNode* j){
		return i->val > j->val;
	}
};
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, comparator> minHeap;
        for(ListNode* node : lists){
            if(node != NULL){
                minHeap.push(node);
            }
        }
        ListNode* head = minHeap.size() == 0 ? NULL : minHeap.top();
        if(head == NULL){
            return head;
        }
        minHeap.pop();
        ListNode* pivot = head;
        if(pivot->next != NULL){
            minHeap.push(pivot->next);
        }
        
        while(minHeap.size() > 0){
            pivot->next = minHeap.top();
            minHeap.pop();
            pivot = pivot->next;
            if(pivot->next != NULL){
                minHeap.push(pivot->next);
            }
        }
        return head;
        
    }
};