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




print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

13. Types of Linked Lists
We'll study these later in detail.
1. Singly Linked List
10 → 20 → 30 → None
Each node points forward.

2. Doubly Linked List
None ← 10 ⇄ 20 ⇄ 30 → None
Each node has:
previous + data + next

3. Circular Linked List
10 → 20 → 30
↑         ↓
└─────────┘
The last node points back to the first node.


"""
print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

problem : 1 : Try to predict the output:

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(5)
b = Node(10)
c = Node(15)

a.next = b
b.next = c

head = a

current = head

while current:
    print(current.data, end=" ")
    current = current.next



print("-------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""


Topic 2 : Node structure & Reference in python 


1. What is a Node?
A Node is an object that stores two main things:
DATA + REFERENCE TO NEXT NODE
Visually:
┌──────────┬──────────┐
│   data   │   next   │
└──────────┴──────────┘
For example:
┌──────┬──────┐
│  10  │   ●──┼────→ next node
└──────┴──────┘
In Python:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

2. Understanding self.data
When we write:
node = Node(10)

the value 10 gets stored in:
node.data

Example:
print(node.data)

Output:
10
So:
node
 ↓
┌──────┬──────┐
│  10  │ None │
└──────┴──────┘
3. Understanding self.next
Initially:
node = Node(10)

we have:
node.next = None
That means:
This node currently doesn't point to another node.

[10 | None]
Later, we can connect it to another node.
4. Connecting Nodes
Create two nodes:
a = Node(10)
b = Node(20)

Initially:
a → [10 | None]

b → [20 | None]
Now:
a.next = b

means:
a
↓
[10 | ●] ─────→ [20 | None]
                 ↑
                 b
So:
a.next

is a reference to object b.
5. Important: next Does NOT Store the Data
This is a common beginner confusion.
Suppose:
a = Node(10)
b = Node(20)

a.next = b

Then:
a.data

is:
10
while:
a.next.data

is:
20
Because:
a.next
  ↓
 b
  ↓
data = 20
6. Understanding a.next.data
This is extremely important.
Consider:
a
↓
[10 | ●] → [20 | ●] → [30 | None]
            ↑
            b
Then:
a.data

→ 10
a.next.data

→ 20
a.next.next.data

→ 30
And:
a.next.next.next

→ None
So:
a
 ↓
a.next
 ↓
a.next.next
 ↓
a.next.next.next
moves one node at a time.


"""



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

head = first


current = head

while current is not None:
    print(current.data)
    current = current.next


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

Topic 3 : Creating a singly linked List





1. What is a Singly Linked List?
A Singly Linked List is a collection of nodes where every node contains:
DATA + NEXT

and each node points only to the next node.
Example:
head
 ↓
[10 | ●] → [20 | ●] → [30 | ●] → [40 | None]

The last node points to:
None


That's why it is called singly linked: each node has only one link to another node.
2. Node Class
First, we need our Node.
class Node:    def __init__(self, data):        self.data = data        self.next = None


When we create:
node = Node(10)


we get:
[10 | None]

3. Why Create a LinkedList Class?
Previously, we manually did:
a = Node(10)b = Node(20)c = Node(30)a.next = bb.next = c


This works, but it's not convenient.
Imagine having 1,000 nodes.
We don't want:
node1
node2
node3
...
node1000

Instead, we'll create a LinkedList class that manages the nodes.
4. Basic LinkedList Class



"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None




print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Insert_at_end() Method 


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node





print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")


