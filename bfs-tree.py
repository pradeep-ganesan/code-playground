"""construct tree and do breadth first search"""

import collections
import unittest

class Node(object):
    def __init__(self, num):
        self.num = num
        self.children = []

    def addchild(self, childnode):
        self.children.append(childnode)

    def getval(self):
        return self.num

def construct_tree(root):
    children = input('children for {} (separated by comma, -1 for end)'.format(
        root.getval())
    )
    if children < 0:
        return
    for num in children:
        if num == -1:
            return

        child = Node(num)
        root.addchild(child)
        construct_tree(child)

def bfssearch(root, target):
    if root.num == target:
        return root
    queue = collections.deque()
    queue.appendleft(root)

    while queue:
        node = queue.pop()
        print node.num
        if node.num == target:
            return node

        queue.extendleft(node.children)

def bfssearchrecur(root, target):
    if root.num == target:
        return root
    queue = collections.deque()
    queue.appendleft(root)
    bfstraverserecur(queue, target)

def bfstraverserecur(queue, target):
    while queue:
        node = queue.pop()
        print node.num
        if node.num == target:
            queue.clear()
            return
        if node.children:
            queue.extendleft(node.children)
            bfstraverserecur(queue, target)

def dfssearch(root, target):
    if root.num == target:
        return root
    queue = collections.deque()
    queue.append(root)

    while queue:
        node = queue.pop()
        print node.num
        if node.num == target:
            return node

        children = list(node.children)
        children.reverse()
        queue.extend(children) 

def dfssearchrecur(root, target):
    if root.num == target:
        return root
    queue = collections.deque()
    queue.append(root)
    dfstraverserecur(queue, target)

def dfstraverserecur(queue, target):
    while queue:
        node = queue.pop()
        print node.num
        if node.num == target:
            queue.clear()
            return node
        if node.children:
            children = list(node.children)
            children.reverse()
            queue.extend(children)
            dfstraverserecur(queue, target)

def main():
    rootnum = input('Root node:')
    root = Node(rootnum)
    construct_tree(root)

    print 'BFS Traversal'
    bfssearch(root, 100)
    print 'BFS Search'
    bfssearch(root, 7)
    print 'BFS Recursive Search'
    bfssearchrecur(root, 7)

    print 'DFS Traversal'
    dfssearch(root, 100)
    print 'DFS Search'
    dfssearch(root, 7)
    print 'DFS Recursive Search'
    dfssearchrecur(root, 7)

if __name__ == '__main__':
    main()
