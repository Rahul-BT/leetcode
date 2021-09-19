# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = ListNode()
        save = out
        while l1 and l2:
            if l1.val < l2.val:
                out.next = l1
                l1 = l1.next
                out = out.next
            else:
                out.next = l2
                l2 = l2.next
                out = out.next
        if l1:
            out.next = l1
            l1 = l1.next
            out = out.next
        elif l2:
            out.next = l2
            l2 = l2.next
            out = out.next
        
        return save.next
        
l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

m3 = ListNode(4)
m2 = ListNode(3, m3)
m1 = ListNode(1, m2)

test = Solution()
print(test.mergeTwoLists(l1,m1))