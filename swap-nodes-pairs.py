# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        root = head
        nxt = head.next
        cont = nxt.next
        nxt.next = root
        root.next = cont
        if cont:
            root.next = self.swapPairs(cont)
        return nxt

if __name__ == '__main__':
    sln = Solution()
    root = node = ListNode(0)
    for x in xrange(6):
        node.val = x
        node.next = ListNode(0)
        prev = node
        node = node.next
    prev.next = None

    def printlist(node):
        while node:
            print node.val
            node = node.next

    print 'original'
    printlist(root)

    print 'swapped'
    root = sln.swapPairs(root)
    printlist(root)