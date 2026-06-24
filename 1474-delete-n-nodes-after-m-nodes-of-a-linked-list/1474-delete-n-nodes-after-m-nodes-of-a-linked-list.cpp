/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteNodes(ListNode* head, int m, int n) {

                
            int remove=0;
            int keep =0;           
            
            ListNode*curr = head;
            ListNode* temp=nullptr;

            while(curr != nullptr)
            {
                keep=0;
                while(keep<m-1 && curr != nullptr)
                {               
                    keep++;
                    curr=curr->next;
                }

                if(curr == nullptr) break;

                temp = curr;
                curr = curr->next;
                
                remove=0;

                while(remove<n && curr != nullptr)
                {               
                    remove++;
                    curr = curr->next;
                }
                temp->next = curr;
            }


            return head;
        
    }
};