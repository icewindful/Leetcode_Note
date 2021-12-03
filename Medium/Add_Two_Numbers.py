# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
### analysis ###
# math method , before next->node save carry value.
# item top pull . val / 10 get carry val , and push to next node.
###   end    ###
class Solution:
    def addTwoNumbers(self, linklist1, linklist2 ,carry = 0):
        """
        :type linklist1: ListNode
        :type linklist2: ListNode
        :rtype: ListNode
        """
        val = linklist1.val + linklist2.val + carry
        carry = val // 10
        ret = ListNode(val % 10 ) 
        
        if (linklist1.next != None or linklist2.next != None or carry != 0):
            if linklist1.next == None:
                linklist1.next = ListNode(0)
            if linklist2.next == None:
                linklist2.next = ListNode(0)
            ret.next = self.addTwoNumbers(linklist1.next,linklist2.next,carry)
        return ret
