# Linked Lists
Sometimes when creating an array, it's hard to know how many items we will include in our array or the right order in which we want to insert the items since the beginning of our project. In such situations, it's very common change our mind or make mistakes and we want to have an easy way to add or delete elements that are not necessary in the beginning or the end of our array. Maybe we want to do it in the middle of our arrangement. If this is our thinking, not many data structures give us this flexibility to easily add elements into our array. However, **Linked lists** allows us to collect data and stored it in memory in a random way. This data structure guarantees us that each element in the list will be stored in some place in memory but not each element will necessarily located in the address next to another element. To understand how it's possible that this data structure keep all the items in the list together, you can read the next section. 

<br> 

## Structure
There are two possible structure a linked list can have. The first type is shown in Figure 2. For this one, each element, also referred as **node**, has an associated **value** and a **pointer** to the address in memory of the **next node** in the list. Usually, the first element in the linked list is called **head**.

<br> 

![Figure 2](Linked_List.png)
<figcaption align = "center"><b>Figure 2 - Linked List</b></figcaption>

<br> 

The second structure that a linked list can have is shown in Figure 3. This one is generally called **doubly-linked list** due to its bi-directional linking property. As you can see in the figure, this arrangement not only has a head but also has a **tail** which is the last element in the list. It additionally counts with pointers to both the address in memory of the next node and **previous node**.


![Figure 3](Doubly-Linked_List.png)
<figcaption align = "center"><b>Figure 3 - Doubly-Linked List</b></figcaption>

<br> 

A powerful property this data structure has is the ability to traverse through the list until we get to the node we want to use for a certain operation. In order to this, it's necessary to know where the head or tail are; that way, we can traverse or reverse traverse until we get to the specific pot where we want to add a new node or remove a node.

<br> 

## How to Insert, Remove and Access Data From a Linked List
The three main operations that can be performed with liked lists are inserting data, removing data and accessing to the data in the list. We will first focus on inserting data to a linked list. 

Inserting a new node in a linked list can be done at the head, tail or middle. Due to that pointers allows us to connect a new node to the next or previous node, the size of the list is not a problem when using this data structure. The processes of inserting at head and tail are very similar. Inserting in the middle can differ from the other two slightly.

### Create a linked list and a new node:
```python
# Linked lists can be implemented in Python by using classes. 
# In case we want to initialize an empty list, we can do it inside the __init__() method declaration of the class.

def __init__(self):
    self.head = None
    self.tail = None

#A new node can be created as an atribute inside a class within the other class

def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

```

<br> 

### Insert a new node in the head: 
```python
# Connect the "next" of the new node to the current head
new_node.next = self.head 

# Connect the "prev" of the current head to the new node
self.head.prev = new_node

# Update the head to point to the new node
self.head = new_node

# SPECIAL CASE
# If linked list is empty, we could just set the head and tail to the new node
if self.head is None:
    self.head = new_node
    self.tail = new_node
```

<br> 

### Insert a new node in the tail: 
```python
# Connect the "prev" of the new node to the current tail
new_node.prev = self.tail 

# Connect the "next" of the current tail to the new node
self.head.prev = new_node

# Update the tail to point to the new node
self.head = new_node
```

<br> 

### Insert a new node in the middle: 
```python
# Connect the "prev" of the new node to the current node
new_node.prev = current 

# Connect the "next" of the new node to the next node after current node
new_node.next = current.next

# Connect the "prev" of the next node after current to the new node
current.next.prev = new_node

# Connect the "next" of the current node to the new node
current.next = new_node
```

<br> 

Removing a node from a linked list can also be done at the head, tail and middle.
### Remove a node from the head: 
```python
# Set the "prev" of the node next to the current head to None
self.head.next.prev = Node

# Update the head to point to the node next to the current head
self.head = self.head.next

# SPECIAL CASE
# If only one node in the list, set the head and tail to None
self.head = None
self.tail = None

```

<br> 

### Remove a node from the tail: 
```python
# Set the "next" of the node previous to the current tail to None
self.tail.prev.next = Node

# Update the tail to point to the node previous to the current tail
self.tail = self.tail.prev
```

<br> 

### Remove a node from the middle: 
```python
# Connect the "prev" of the node after current to the node before current
current.next.prev = current.prev

# Connect the "next" of the node before current to the node after current
current.prev.next = current.next
```

<br> 

Whenever we want to access to data in the list, we need to traverse the list starting by the head or the tail. This can be done by using a while loop and following the "next" or "prev" linked node until we get to the value we are trying to find or the end of the list.

### Access a node from the linked list: 
```python
# Check if an specific value is in the list
def find_value(self, value):

    # Whenever we want to start at the head
    current = self.head

    # Loop as long as we haven't reach the value we want
    while current is not value:
        
        # Point to the next node
        current = current.next

    # Print the value once it's found
    print(current.data)
```
If we want to loop through the list starting at the tail we just need to change the lines of code  `current = self.head` to `current = self.tail` and `current = current.next` to `current = current.prev`.

<br> 

## Python Syntax
Besides the methods previously mentioned for the implementation of the linked list, Python also has a built-in linked list already. The commands to use this linked list are the following:

* >``` linked_list = deque() ```: It creates a empty linked list
* >``` linked_list.appendleft(value) ```: It inserts a new head
* >``` linked_list.append(value) ```: It inserts a new tail
* >``` linked_list.insert(i, value) ```: It inserts a new value after the node "i"
* >``` data = linked_list.popleft() ```: It removes the head and stores it in a variable
* >``` data = linked_list.pop() ```: It removes the tail and stores it in a variable
* >``` del linked_list[i] ```: It removes a value in the middle of the list
* >``` length = len(list) ```: It returns the size of the linked list
* >``` if len(list) = 0 ```: It checks if the linked list is empty. If it's, it returns true

## Example

## Problem to Solve

[Back to Welcome Page](1-welcome.md)