/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode temp, prev, after;
        ListNode ans = head;
        
        if (head != null && head.next != null){
            ans = head.next;
            
            prev = head;
            after = head.next;
            temp = after.next;
            after.next = head;
            head.next = temp;
            
            while (temp != null ){
                if (temp.next != null){
                    prev.next = temp.next;
                    prev = temp;
                    after = temp.next;
                    head = after.next;
                    after.next = temp;
                    temp.next = head;
                    temp = head;
                    
                }else{
                    prev.next = temp;
                    temp = temp.next;
                }
            }
        }
        
        return ans;
        
    }
}
