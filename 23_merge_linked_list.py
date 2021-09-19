# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        out = []
        for lis in lists:
            while lis:
                out.append(lis.val)
                lis = lis.next
        
        if len(out) == 0:
            return None
        
        out.sort()
        head = ListNode(out[0])
        t_ = head
        for i in out[1:]:
            head.next = ListNode(i)
            head = head.next
        
        return t_

        



        
l3 = ListNode(5)
l2 = ListNode(4,l3)
l1 = ListNode(1,l2)

m3 = ListNode(4)
m2 = ListNode(3,m3)
m1 = ListNode(1,m2)

n2 = ListNode(6)
n1 = ListNode(2,n2)

o2 = ListNode(4)
o1 = ListNode(1,o2)

test = Solution()
ans = test.mergeKLists([])

while ans:
    print(ans.val)
    ans = ans.next


        