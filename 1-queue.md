# Queues
A queue is data structure that allows the user to organize and store data in a "First In, First Out" (FIFO) configuration. This data structure is commonly represented as a line of people waiting to be served. In this arrangement, the person who joined the line first is the one who is served first. This data structure is useful whenever we want to process a group of requests or data in order of arrival. Some common queue applications are routers, print management, interrupts handling on some operating systems, or website traffic handling, among others.

## Structure
In order to understand the structure of a queue, we can consider the following example: <br> 
<br> 
Imagine that there are several people in line at a bank ready to be served. The person who joined the line the earliest is called the **front**, and the person who joined the line the last is called the **back**. When the person at the front of the line is served, and therefore removed from the queue, we call this operation **dequeue**. When a new person arrives at the bank and lines up, we call this operation **enqueue**.
<br> 
<br> 
![Figure 1](Queue.png)
<figcaption align = "center"><b>Figure 1 - Queue</b></figcaption>
<br> 
A queue is fairly simple data structure, but it can be a powerful tool when using adequately.

## Reading From and Writing to a Queue
Whenever we want to read from a queue, we can implement a line of code like this:

<br> 

```
#This line of code deletes the item in the front of the queue and store it in a variable

data = list.pop(0)

#Another way to implement this same operation would be

data = list[0]
del list[0]

```

This would allow us to dequeue the front value and store it in a variable. Once the value is stored in a variable, we can use this variable for any other operations needed.
<br> 
<br> 
Whenever we want to write to a queue, we can implement the following line of code: 

```
#This line of code appends a new item to the back of the queue

list.append(item)

```
This would allow us to enqueue a new value to the back of the queue.


## Python Syntax
As we could see in the previous section, a queue can be implemented on Python by using a list. 
The following pieces of code can be used to implement a queue in Python:
<br> 

* >``` list.append(item) ```: It adds a new item to the back of the queue
* >``` data = list.pop(0) ```: It removes and return the item at the front of the queue
* >``` length = len(list) ```: It returns the size of the queue
* >``` if len(list) = 0 ```: It checks if the queue is empty. If it's, it returns true


## Example

## Problem to Solve

[Back to Welcome Page](1-welcome.md)