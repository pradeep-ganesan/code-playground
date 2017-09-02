# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = lsum = ListNode(0)
        carry = 0
        last = None
        while l1 and l2:
            prev = lsum
            lsum.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10
            lsum.next = ListNode(0)
            lsum = lsum.next

            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None:
            if carry:
                lsum.val = carry
            else:
                prev.next = None
            return head

        l = l1 or l2
        while l:
            lsum.val = (l.val + carry) % 10
            carry = (l.val + carry) / 10
            l = l.next
            lsum.next = ListNode(0)
            last = lsum
            lsum = lsum.next

        if carry:
            lsum.val = carry
        else:
            last.next = None
            lsum = None

        return head

def additem(head, item):
    l = head
    if not l:
        l = ListNode(item)
        return l

    while l:
        last = l
        l = l.next

    last.next = ListNode(item)
    return head

def printl(l):
    while l:
        print l, l.val, l.next
        l = l.next

def main():
    sln = Solution()
    head1 = None
    head2 = None
    for x in [2,4,3]:
        head1 = additem(head1, x)
    for x in [5,6,4]:
        head2 = additem(head2, x)

    add = sln.addTwoNumbers(head1, head2)
    printl(add)

if __name__ == '__main__':
    main()