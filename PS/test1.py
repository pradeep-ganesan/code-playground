class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def print_singly_linked_list(head):
    tmp = head
    while tmp != None:
        print tmp.val
        tmp = tmp.next_node

def add_to_singly_linked_list(head, val):
    tmp = head
    while tmp.next_node != None:
        tmp = tmp.next_node
    tmp.next_node = Node(val)

def remove_all_n(head, n):
    # Fill in the logic here
    while head and head.val == n:
        # delete initial nodes with 'n'
        cur = head
        head = head.next_node
        del cur

    cur = head
    while cur and cur.next_node:
        if cur.next_node.val == n:
            rem = cur.next_node
            cur.next_node = rem.next_node
            del rem
        tmp = cur
        cur = cur.next_node
    if cur and cur.val == n:
        # last node
        tmp.next_node = None
        del cur
    
    return head

def main():
    inp = raw_input().split()
    n = inp.pop(0)
    size = inp.pop(0)
    head = Node(inp.pop(0))
    while inp: add_to_singly_linked_list(head, inp.pop(0))
    head = remove_all_n(head, n)
    print_singly_linked_list(head)

if __name__=="__main__":
    main()