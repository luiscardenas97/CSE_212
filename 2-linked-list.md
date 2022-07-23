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

## Example: List of Student Enrolled in a Class
In the example below, we will write a simple program that create a linked list with the names of all the students enrolled in a circuits class. This linked list will allow the instructor add new student to the course in the order he or she wishes; therefore, the program should allow him or her to add at the beginning, middle or end of the list. Despite that there is already a built-in class on Python to create a linked list, we will use our knowledge on object-oriented programming to come up with our own class to do this. The specifications for the program are the following:
* Add new students to the beginning or end of the linked list
* Add new student after another specific student
* Remove student at the beginning, end or middle of the linked list
* Print the linked list with the student enrolled in the class
* Print a message when the student try to remove a student from an empty list

<br> 

```python
import string

# Create class that will contain the linked list
class EnrolledList:
    # Create class that will contain each student name as a node
    class Student_Name:
        def __init__(self, student_name):
            self.student_name = student_name
            self.next_student = None
            self.previous_student = None
    
    # Create a empty linked list
    def __init__(self):
        self.first_student = None
        self.last_student = None

    # Method that allows the user add a new student at the beginning of the list
    def insert_student__at_front(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        # If linked list is empty, add new student at the beginning of the list
        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        # Otherwise, add new student at the beginning of the link by making old first student, the second student in the list
        else:
            new_student.next_student = self.first_student
            self.first_student.previous_student = new_student
            self.first_student = new_student

    # Method that allows the user add a new student at the end of the list
    def insert_student_at_end(self, student_name):
        new_student = EnrolledList.Student_Name(student_name)

        # If linked list is empty, add new student at the end of the list
        if self.first_student is None:
            self.first_student = new_student
            self.last_student = new_student

        # Otherwise, add new student at the end of the link by making old last student, the second to last student in the list
        else:
            new_student.previous_student = self.last_student
            self.last_student.next_student = new_student
            self.last_student = new_student

    # Method that allows the user add a new student after another student
    def insert_student_after(self, student_name, enrolling_student):
        # Starting from the first student in the linked list, loop through each student until it finds the student after which new student will be added
        current_student = self.first_student
        # If linked list is not empty, keep looping through the list
        while current_student is not None:
            # Check if the current student in the list is the same as the student after which the new student will be added. If it's, add new student after the current student
            if current_student.student_name == student_name:
                # If current student is the same as the last student, add new student at the end of the linked list
                if current_student == self.last_student:
                    self.insert_student_at_end(enrolling_student)
                # Add new student after the current student
                else:
                    new_student = EnrolledList.Student_Name(enrolling_student)
                    new_student.previous_student = current_student
                    new_student.next_student = current_student.next_student
                    current_student.next_student.previous_student = new_student
                    current_student.next_student = new_student

            # Go to next student in the list    
            current_student = current_student.next_student

    # Method that allows the user remove a student from the linked list at the beginning of the list
    def remove_student_at_front(self):
        # If there is only one student in the linked list, remove that student
        if self.first_student == self.last_student:
            self.first_student = None
            self.last_student = None
        # As long as the linked list is not empty, remove student at the beginning of the list
        elif self.first_student is not None:
            self.first_student.next_student.previous_student = None
            self.first_student = self.first_student.next_student

    # Method that allows the user remove a student from the linked list at the end of the list
    def remove_student_at_end(self):
        # If there is only one student in the linked list, remove that student
        if self.first_student == self.last_student:
            self.first_student = None
            self.last_student = None
        # As long as there is a last student, remove student at the beginning of the list
        elif self.last_student is not None:
            self.last_student.previous_student.next_student = None
            self.last_student = self.last_student.previous_student

    # Method that allows the user remove a student from the linked list at the middle of the list
    def remove_student_in_middle(self, student_name):
        # Starting from the first student in the linked list, loop through each student until it finds the student that will be removed
        current_student = self.first_student
        # If linked list is not empty, keep looping through the list
        while current_student is not None:
            # Check if the current student in the list is the same as the student that will be remove. If it's, remove the student
            if current_student.student_name == student_name:
                # If current student is the first one in the list, remove that student
                if current_student.student_name == self.first_student.student_name:
                    self.remove_student_at_front()
                # If current student is the last one in the list, remove that student
                elif current_student.student_name == self.last_student.student_name:
                    self.remove_student_at_end()
                # As long as the current student is not the same as the first student, remove that student
                elif current_student.student_name != self.first_student.student_name:
                    current_student.next_student.previous_student = current_student.previous_student
                    current_student.previous_student.next_student = current_student.next_student
                return
            # Go to next student
            current_student = current_student.next_student
        # If linked list is empty, print message
        if current_student == None and current_student.student_name == student_name:
            print("We're sorry, but you can remove the student. The list is empty.")

    # Iterate through the linked list. Allow the user to use 'for' loop
    def __iter__(self):
        # Starting from the first student in the linked list, iterate through each student in the list
        current_student = self.first_student
        # As long as the end of the list is not reached, keep looping
        while current_student is not None:
            # Return the name of the current student
            yield current_student.student_name
            # Go to next student
            current_student = current_student.next_student

    # Method that allow to print the student in the linked list as string
    def __str__(self):
        student_list = "Enrolled Students for Circuits Class: \n"
        for student in self:
            student_list += student
            student_list += "\n"
        
        return student_list

student_list = EnrolledList()

exit_menu = "no"

# Create menu that allow user to perform different operations with the linked list
while exit_menu == "no":
    request = 1
    print("Enrolled List Menu: ")
    print("1) Add student to enrolled list at beginning or end of the list")
    print("2) Add student to enrolled list after an specific student")
    print("3) Remove student from enrolled list")
    print("4) Print list of students enrolled in the course")
    print("5) Exit")
    operation = int(input("\nSelect operation: "))

    # Add new student at the beginning or end of the linked list
    if operation == 1:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords(student_name)
            order = input("\nDo you want to add new student at the beginning or end of the list (Enter 1 for beginning or 0 for end)? ")
            if order == 1:
                student_list.insert_student__at_front(student_name_format)
            else:
                student_list.insert_student_at_end(student_name_format)
            
            request = int(input("\nDo you want to add another student at the beginning or end of the enrolled list? (Enter 1 for yes and 0 for no): "))

    # Add new student to the linked list after an specific student
    elif operation == 2:
        while request == 1:
            student_name = input("\nPlease introduce the name of the new student you want to add to the enrolled list: ")
            student_name_format = string.capwords (student_name) # Convert the string with the student name to the right format
            previous_student = input("\nPlease introduce the name of the student after which you want to add the new student: ")
            previous_student_format = string.capwords(previous_student) # Convert the string with the student name to the right format
            student_list.insert_student_after(previous_student_format, student_name_format)

            request = int(input("\nDo you want to add another student at the middle of the enrolled list? (Enter 1 for yes and 0 for no): "))

    # Remove student from linked list
    elif operation == 3:
        while request == 1:
            student_name = input("\nPlease introduce the name of the student you want remove from the enrolled list: ")
            student_name_format = string.capwords(student_name) # Convert the string with the student name to the right format
            student_list.remove_student_in_middle(student_name_format)

            request = int(input("\nDo you want to remove another student from the enrolled list? (Enter 1 for yes and 0 for no): "))

    # Print linked list    
    elif operation == 4:
        print()
        print(student_list)

    # Exit the menu
    elif operation == 5:
        exit_menu = "yes"
    
    print()
```


## Problem to Solve

You can check your work with the solution here: [Solution](enrolled_list.py)

[Back to Welcome Page](1-welcome.md)