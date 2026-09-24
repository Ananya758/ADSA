'''
Singly Linked List:
Algorithm:
1. create node 
2. Insert the data into the nodes
3. Generate the connection btw the nodes
4. Traverse all the nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.nexr = node4

def traverse():
    curr = node1
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")
traverse()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
print("Insertion at the begin")
traverse(head)

def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
'''
'''
deletion 3 ways:
a) deletion at the beginning
b) deletion at the end
c) deletion at a specific node
'''
def deletion_begin(head):
    if head is None:
        print("Error")
        return
    new_head = head.next
    del head
    return new_head

def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    del_node = curr.next
    curr.next = None
    del del_node

def deletion_at_pos(node):
    if node is None or node.next is None:
        print("Error")
        return None
    next_node = node.next
    node.next = next_node.next
    del next_node

