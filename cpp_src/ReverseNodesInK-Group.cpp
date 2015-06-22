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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k == 0){
            return head;
        }
        ListNode* fakeHead = new ListNode(0);
        fakeHead->next = head;
        //the last node that we have reversed
        ListNode* preNode = fakeHead;
        //the last node that we are reserving;
        ListNode* last = fakeHead;
        while(last != NULL){
            last = last->next;
            head = last;
            //after call reverseKNodes, the head will point to the new head of K nodes
            last = reverseKNodes(head,k);
            preNode->next = head;
            preNode = last;
        }
        return fakeHead->next;
    }
    
    //return last node of the K nodes
    ListNode* reverseKNodes(ListNode*& head, int k){
        stack<ListNode*> nodesStack;
        int num = 0;
        ListNode* pivot = head;
        while(num < k && pivot != NULL){
            nodesStack.push(pivot);
            pivot = pivot->next;
            num++;
        }
        if(num == k){
            //the next of the last node
            ListNode* last = pivot;
            //the first of the K nodes;
            head = nodesStack.top();
            nodesStack.pop();
            pivot = head;
            while(!nodesStack.empty()){
                pivot->next = nodesStack.top();
                nodesStack.pop();
                pivot = pivot->next;
            }
            pivot->next = last;
            return pivot;
        }else{
            return NULL;
        }
    }
};