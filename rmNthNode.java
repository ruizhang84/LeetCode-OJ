/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode tmpStore = head;
        ListNode tmpPrev = head;
        ListNode tmp = head;
        
        for (int i = 1; i < n; i++)
            tmp = tmp.next;
        
        while (tmp.next != null){
            tmp =tmp.next;
            tmpPrev = tmpStore;
            tmpStore = tmpStore.next;
            
        }
        
        if (tmpStore == head)
            return head.next;
        
        tmpPrev.next = tmpStore.next;
            
        return head;
        
    }
}
