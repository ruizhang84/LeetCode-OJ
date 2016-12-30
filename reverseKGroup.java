/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || head.next == null)
            return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        head = dummy;
        while (head.next != null)
            head = help_reverseKGroup(head, k);
        
        
        return dummy.next;
        
    }
    
    public ListNode help_reverseKGroup(ListNode head, int k) {
        ListNode next = head;
        
        for (int i = 0; i < k; i++){
            if (next.next == null)
                return next;
            
            next = next.next;
            
        }
        
        ListNode n1 = head.next;
        ListNode prev = head, curt = n1;
        for (int i = 0; i < k; i++){
            ListNode temp = curt.next;
            curt.next = prv;
            prv = curt;
            curt = temp;
            
        }
        
        n1.next = curt;
        head.next = prev;
        
        
        return n1;
        
    }

    
    
}
