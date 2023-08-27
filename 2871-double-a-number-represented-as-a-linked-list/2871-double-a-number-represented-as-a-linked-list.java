/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode doubleIt(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;


        while(curr!=null){
            if(curr.val >= 5){
                curr.val = (curr.val*2)%10;
                if(prev == null){
                    prev = new ListNode(1);
                    prev.next = curr;
                    head = prev;
                }
                else{
                    prev.val+=1;
                }
            }
            else{
                curr.val *=2 ;
            }

            prev = curr;
            curr = curr.next;
        }

        return head;
        
    }
}