#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1:ListNode , l2:ListNode ):
        
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            print(val1)
            val2  = (l2.val if l2 else 0)
            print(val2)
            carry, out = divmod(val1+val2 + carry, 10)
            #print(carry,out)
            """
            divmod : example number , 11 : out = 15/10 (get last) = 5 / carry = 15/10 ( get first ) = 1
            """          
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = ListNode(0)

Solution.addTwoNumbers(l3,l1,l2)
    