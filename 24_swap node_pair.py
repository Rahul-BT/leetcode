# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printVal(self):
        print(self.val)

    def traverse(self):
        head = self
        out = []
        while head:
            out.append(head.val)
            head = head.next
        print(out)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        out = []
        while head:
            out.append(head.val)
            head = head.next
        
        i=0
        while i< len(out)-1:
            temp = out[i+1]
            out[i+1] = out[i]
            out[i] = temp
            i += 2
        
        head = ListNode(out[0])
        p = head
        for i in out[1:]:
            head.next = ListNode(i)
            head = head.next
        
        return p

    def swapPairs2(self,head):
        if head.next == None:
            return head
        origin = ListNode(0, head)
        ret = origin
        
        print("Next: {}".format(origin.next.next.val))
        while origin.next.next:
            t1 = origin.next
            t2 = t1.next
            t3 = t2.next

            origin.next = t2
            t2.next = t1
            t1.next = t3

            #ret.traverse()
            #print(t1.val)
            origin = t1
            if origin.next == None:
                break
            #print("Next: {}".format(origin.next.next.val))

        
        return ret.next
        
l6 = ListNode(6)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
l1.traverse()
test = Solution()
ans = test.swapPairs2(l6)
print()
ans.traverse()