"""

Topic 1: introduction to linked list 

1. What is a Linked List?
A Linked List is a linear data structure where elements are stored inside separate objects called nodes.

Each node normally contains:
DATA + REFERENCE


Example:
[10 | next] → [20 | next] → [30 | next] → NULL
Here:
- 10, 20, 30 → data
- next → reference to the next node
- NULL / None → there is no next node




2. Array vs Linked List
You already studied arrays, so this comparison is very important.
Array
[10] [20] [30] [40]
Elements are accessed using an index:
arr[2]

Output:
30
Linked List
[10] → [20] → [30] → [40] → None
There is no direct index-based access like an array.
To reach 30, we normally start from the first node and follow the links:
10 → 20 → 30

3. Why Do We Need Linked Lists?
Suppose we have:
[10, 20, 30, 40]
If we insert 5 at the beginning of an array:
[5, 10, 20, 30, 40]
Existing elements may need to be shifted.
With a linked list:
Before:

10 → 20 → 30 → 40
Create a new node:
5
Connect it:
5 → 10 → 20 → 30 → 40
The links are changed instead of shifting every existing element.
That's one of the major advantages of linked lists.
4. Node Concept 
The most important concept in Linked List is the Node.
A node contains:
┌─────────┬──────────┐
│  DATA   │   NEXT   │
└─────────┴──────────┘
Example:
┌──────┬──────┐
│  10  │  ●───┼─────→ next node
└──────┴──────┘
For three nodes:
┌────┬─────┐    ┌────┬─────┐    ┌────┬──────┐
│ 10 │  ●──┼──→ │ 20 │  ●──┼──→ │ 30 │ None │
└────┴─────┘    └────┴─────┘    └────┴──────┘
5. What is head?
The head is a reference pointing to the first node.
head
 ↓
[10] → [20] → [30] → None
If:
head = None

then the Linked List is empty.
head
 ↓
None
Important
We normally don't need to store references to every node separately.
We only need:
head
 ↓
first → second → third → None
Each node knows where the next node is.
6. Creating a Node in Python
Python doesn't have a built-in traditional Linked List class, so we create our own.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Now create a node:
node1 = Node(10)

It looks conceptually like:
node1
 ↓
┌────┬──────┐
│ 10 │ None │
└────┴──────┘
7. Connecting Two Nodes
node1 = Node(10)
node2 = Node(20)

node1.next = node2

Now:
node1
 ↓
[10] → [20] → None
          ↑
        node2
8. Creating a Three-Node Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

Structure:
head
 ↓
[10] → [20] → [30] → None
9. Traversing the Linked List
Traversal means:
Visit every node one by one.

Start from head.
current = head

Then:
current
   ↓
[10] → [20] → [30] → None
Move:
current = current.next

Now:
[10] → [20] → [30] → None
        ↑
      current
Continue until:
current is None

10. Complete Traversal Program


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1


current = head

while current is not None:
    print(current.data)
    current = current.next