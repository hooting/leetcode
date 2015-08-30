/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 /**
  * divide list into two lists: one is < x, the other is >= x,
  * then append the second list to the tail of the first one
  */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode head1 = new ListNode(0);
        ListNode tail1 = head1;
        ListNode head2 = new ListNode(0);
        ListNode tail2 = head2;
        for(;head != null; head = head.next){
            if(head.val < x){
                tail1.next = head;
                tail1 = head;
            }else{
                tail2.next = head;
                tail2 = head;
            }
        }
        tail1.next = head2.next;
        tail2.next = null;
        return head1.next;
    }
}