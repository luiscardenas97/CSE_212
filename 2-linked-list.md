# Linked Lists
Sometimes when creating an array, it's hard to know how many items we will include in our array or the right order in which we want to insert the items since the beginning of our project. In such situations, it's very common change our mind or make mistakes and we want to have an easy way to add or delete elements that are not necessary in the beginning or the end of our array. Maybe we want to do it in the middle of our arrangement. If this is our thinking, not many data structures give us this flexibility to easily add elements into our array. However, **Linked lists** allows us to collect data and stored it in memory in a random way. This data structure guarantees us that each element in the list will be stored in some place in memory but not each element will necessarily located in the address next to another element. To understand how it's possible that this data structure keep all the items in the list together, you can read the next section. 

## Structure
There are two possible structure a linked list can have. The first type is shown in Figure 1. For this one, each element, also referred as **node**, has an associated **value** and a **pointer** to the address in memory of the **next node** in the list. Usually, the first element in the linked list is called **head**.

<br> 

![Figure 1](Linked_List.png)
<figcaption align = "center"><b>Figure 2 - Linked List</b></figcaption>

<br> 

The second structure that a linked list can have is shown in Figure 2. This one is generally called **doubly-linked list** due to its bi-directional linking property. As you can see in the figure, this arrangement not only has a head but also has a **tail** which is the last element in the list. It additionally counts with pointers to both the address in memory of the next node and **previous node**.


![Figure 1](Doubly-Linked_List.png)
<figcaption align = "center"><b>Figure 3 - Doubly-Linked List</b></figcaption>

<br> 

A powerful property this data structure has is the ability to traverse through the list until we get to the node we want to use for a certain operation. In order to this, it's necessary to know where the head or tail are; that way, we can traverse or reverse traverse until we get to the specific pot where we want to add a new node or remove a node.

## How to Insert, Remove and Access Data From a Linked List


## Python Syntax

## Example

## Problem to Solve

[Back to Welcome Page](1-welcome.md)