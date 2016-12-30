/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(0);
        ListNode head = l3;
        
        while (l1 != null && l2 != null){
            if (l1.val <= l2.val){
                head.next = l1;
                l1 = l1.next;
                head = head.next;
                
            }else{
                head.next = l2;
                l2 = l2.next;
                head = head.next;
            }
            
        }
        
        
        while (l1 != null){
            head.next = l1;
            l1 = l1.next;
            head = head.next;
            
        }
        
        while (l2 != null){
            head.next = l2;
            l2 = l2.next;
            head = head.next;
            
        }
        
        
        return l3.next;
    }
}
