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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode first(0);
        ListNode* result = &first;
        
        while (l1 && l2) {
            result->next = new ListNode((l1->val+l2->val+carry)%10);
            carry = (l1->val+l2->val+carry)/10;
            
            l1 = l1->next;
            l2 = l2->next;
            result = result->next;
        }
        
        ListNode* l3 = (l1 == NULL)?l2:l1;
            
        while (l3) {
            result->next = new ListNode((l3->val+carry)%10);
            carry = (l3->val+carry)/10;
            
            l3 = l3->next;
            result = result->next;
        }

        if (carry > 0) result->next = new ListNode(1);

        return first.next;
        
    }
};