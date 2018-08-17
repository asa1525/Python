# Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(5)
root.left  = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(7)
root.left.right = TreeNode(2)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(0)
root.right.right.right = TreeNode(8)

def getMax(node):
    if not node:
        raise Exception('Empty')
    tree_max =node.val
    if node.left:
        tree_max = max(tree_max, getMax(node.left))
    if node.right:
        tree_max = max(tree_max, getMax(node.right))
    return tree_max

print('Get Max:', getMax(root))
print('\n')


## Singly linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(8)
    
def getSum(node):
    if not node:
        raise Exception('Empty')
    list_sum = node.val
    if node.next:
        list_sum += getSum(node.next)
    return list_sum

print('Get Sum:',getSum(head))
print('\n')


### Stack

stack = []
stack = []
stack.append(1) # push 1
stack.append(2) # push 2
stack.append(3) # push 3
while stack:
    print('Stack:')
    print(stack[-1])
    print(stack.pop())
print('\n')


#### Queue

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

while queue:
    print('Queue:', queue.popleft())
print('\n')

##### Priority queue
from heapq import heappush, heappop
queue = []
heappush(queue, 3) # 插入1
heappush(queue, 2) # 插入2
heappush(queue, 1) # 插入1

while queue:
    print(queue[0])
    print(heappop(queue))
print('\n')

# Exercise: Sum of BT
def getBtSum(node):
    tree_sum = node.val
    if node.left:
        tree_sum += getBtSum(node.left)
    if node.right:
        tree_sum += getBtSum(node.right)
    return tree_sum

print(getBtSum(root))

# Exercise2: use ListNode to run a class Stack
## use dummy
class Stack:
    def __init__(self):
        self.dummy = ListNode(-1)

    def push(self, val):
        old_head = self.dummy.next
        new_head = ListNode(val)
        new_head.next = old_head
        self.dummy.next = new_head

    def pop(self):
        if not self.dummy.next:
            raise Exception('Popping from empty stack is not allowed.')
        popped = self.dummy.next
        self.dummy.next = self.dummy.next.next
        return popped.val
    
    def peek(self):
        if not self.dummy.next:
            raise Exception('Peeking from empty stack is not allowed.')
        return self.dummy.next.val

    def isEmpty(self):
        return self.dummy.next is None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
while not stack.isEmpty():
    print(stack.peek())
    print(stack.pop())