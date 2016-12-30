/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
        return recur_mergeKLists(lists);
        
    }
    
    
    public ListNode recur_mergeKLists(ListNode[] lists) {
        int size = lists.length;
        
        if (size == 2)
            return mergeTwoLists(lists[0], lists[1]);
        else if (size == 1)
            return lists[0];
        else if (size == 0)
            return null;
        
        
        ListNode[]  newLists1 = Arrays.copyOfRange(lists, 0, size/2);
        ListNode[]  newLists2 = Arrays.copyOfRange(lists, size/2, size);
        
        ListNode l1 = recur_mergeKLists(newLists1);
        ListNode l2 = recur_mergeKLists(newLists2);
        
        return mergeTwoLists(l1, l2);
        
    }
    
    
    
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
