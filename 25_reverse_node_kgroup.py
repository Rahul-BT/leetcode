# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self):
        head = self
        out = []
        while head:
            out.append(head.val)
            head = head.next
        print(out)

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        c_ = 0
        t_ = []
        ori = head
        
        # Add the nodes to a list : [1*, 2*, 3*]
        while c_<k:
            if not head:
                # If #nodes less than "k-group", return the head
                return ori
            t_.append(head)
            head = head.next
            c_ +=1
        c_ -=1
        
        # Reverse the .next value of the node : [ ?<- 1 <- 2 <-3]
        while c_>0:
            t_[c_].next =  t_[c_-1]
            c_ -=1

        if head:
            # If nodes are remanining, call the fn with the rem. nodes
            n_head = self.reverseKGroup(head,k)
            # Link the rem. reversed node to t_[0]
            # t_: [ ?<-1<-2<-3], n_head = [4<-5<-6] Replace "?" with 6* (ie n_head)
            t_[0].next = n_head
        else:
            # If no rem. nodes, Link NONE to t_[0]
            # [ None<- 1 <- 2 <-3]
            t_[0].next = None
        
        # Return the last node of t_ (ie 3*)
        return t_[-1]



l6 = ListNode(6)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

l1.traverse()

test = Solution()
ans = test.reverseKGroup(l1,4)

ans.traverse()