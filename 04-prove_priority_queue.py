"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority) # Error Found: It had the arguments switched
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority: #Error Found: It changed the high_pri_index even if two nodes had the same highest priority
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index] #Error Found: It didn't remove the node from the queue
        
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Create a queue with the following nodes and priorities: Node 1 (4), Node 2 (2), Node 3 (5) and run until the queue is empty.
# Expected Result: Node 3, Node 1, Node 2
print("Test 1")
nodes = Priority_Queue()
nodes.enqueue("Node 1", 4)
nodes.enqueue("Node 2", 2)
nodes.enqueue("Node 3", 5)
print(nodes)
while len(nodes) > 0:
    print(nodes.dequeue())
    
# Defect(s) Found: It had the input arguments switched on the class call inside the enqueue method, causing the node name 
# to be used as the priority and the priority to be used as the node name, and it wasn't removing nodes from the queue.

print("=================")

# Test 2
# Scenario: Create a queue with the following nodes and priorities: Node 1 (4), Node 2 (7), Node 3 (5), Node 4 (7), Node 5 (2) and run until 
#   the queue is empty. Two of the nodes have the highest priority.
# Expected Result: Node 2, Node 4, Node 3, Node 1, Node 5
print("Test 2")
nodes = Priority_Queue()
nodes.enqueue("Node 1", 4)
nodes.enqueue("Node 2", 7)
nodes.enqueue("Node 3", 5)
nodes.enqueue("Node 4", 7)
nodes.enqueue("Node 5", 2)
print(nodes)
while len(nodes) > 0:
    print(nodes.dequeue())
# Defect(s) Found: When two of the nodes have the highest priority, it wasn't removing the item closest to the front of the queue.

print("=================")

# Test 3
# Scenario: Try to get the next node from an empty queue
# Expected Result: Error message "The queue is empty." should be displayed
print("Test 3")
nodes = Priority_Queue()
print(nodes)
nodes.dequeue()
# Defect(s) Found:  No defect was found in this test. It displayed the error message as expected. 

print("=================")

# Test 4
# Scenario: Create a queue with the following nodes and priorities: Node 1 (1), Node 2 (7), Node 3 (5)
#   After running 2 times, add Node 4 with priority 3 and Node 5 with priority 8. Run until the queue is empty. 
# Expected Result: Node 2, Node 3, Node 5, Node 4, Node 1
print("Test 4")
nodes = Priority_Queue()
nodes.enqueue("Node 1", 1)
nodes.enqueue("Node 2", 7)
nodes.enqueue("Node 3", 5)
#print(nodes)
for i in range(2):
    print(nodes.dequeue())
nodes.enqueue("Node 4", 3)
nodes.enqueue("Node 5", 8)
#print(nodes)
while len(nodes) > 0:
    print(nodes.dequeue())
# Defect(s) Found: No defect was found in this test. It displayed the nodes in the right order.
