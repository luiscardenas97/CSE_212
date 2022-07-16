# Trees
While working with directories or file systems, we might occasionally be interested in organizing our data in a hierarchical order. We might want to have the most significant item or origin in the top and less relevant elements in sublevels. Most data structures provide a linear configuration to insert or arrange data; however, one of the data structures that allow the user to apply a hierarchical arrangement is called **Tree**. This organizational format works similar to a linked list due to it uses pointers, also called edges, to connect nodes. One big difference, though, is that this structure allows connecting more than one node to the tree at the same level. How this data structure grows is by creating branches where we can store more data, and each branch can have multiple branches just like a tree, hence the name. Next section provides more details on how this structure is formed.

<br> 

## Structure
There are several types of trees we could talk about; however, we will limit our study to only three of them. We would like to begin by introducing the binary trees. Unlike a general tree that can multiple nodes per level, a **binary tree** can only allocate two nodes per sublevel and each branch created by each of these two nodes can only have two other subnodes and so forth. Hence the name binary tree. The node from where our binary tree begins, origin or top, is commonly known as **root**. The branches created by the subnodes are called **subtrees**. Most of the nodes have a parent-child relationship. The subnode connected to an upper node is usually called **child** and the upper node to which the subnode is connected is called **parent**. Each child node, as mentioned previously, generally forms a subtree. Nodes that don't have any children are called **leaves**. The links used to connect one node to another are called **edges**; they are usually represented as arrows or lines in the diagrams. Another term that would relevant to define is the height of a tree. The **heigh of a tree** is the number of nodes through the path with the maximum number of nodes from the root to a leaf. Despite this definition only applies to the entire tree, the height of a subtree can be calculated in the same way. All of these elements can be observed in the Figure 4.

<br>

![Figure 4](Binary_Tree.png)
<figcaption align = "center"><b>Figure 4 - Binary Tree</b></figcaption>

<br>

A binary tree can also be classified into two other categories, a full binary tree and a complete binary tree. A **full binary tree** is when each node of the tree is restricted to have only zero or two children. A child per node is not allowed. A **complete binary tree** is when each level of the tree is entirely filled; the last level could be an exception to this rule. The Figure 5 shows some examples of these two subcategories.

<br>

![Figure 5](Full_Complete_Binary_Tree.png)
<figcaption align = "center"><b>Figure 5 - Full Binary Tree / Complete Binary Tree </b></figcaption>

<br>

The second type of tree structure we will introduce is the **binary search tree (BST)**. This one has more restrictions than the one introduced previously. In a BST type of structure, data that is smaller than the parent node, starting at the root, is stored as a subtree in the left side, and data that is larger is stored as a subtree in the right side. Whenever we have data that is repeated, it can be added either to the right or left. BSTs are very efficient when it comes to searching for data because of its O(log n) performance. A O(log n) is a big O notation assigned to programs or data structures that have the performance of a base 2 logarithmic function. In other words, algorithms that are able to reduce the number of operations required to perform to the half each iteration. This is a property that allows the users to reduce the job by 50% at each level whene trying to find an empty spot to add data in a BST. The Figure 6 and 7 show a BST and its typical operation.

<br>

![Figure 6](BST.png)
<figcaption align = "center"><b>Figure 6 - Binary Search Tree (BST) </b></figcaption>

<br>

<br>

![Figure 7](BST_performance.png)
<figcaption align = "center"><b>Figure 7 - BST Typical Operation </b></figcaption>

<br>

Finally, we want to introduce the type of tree structure called **balanced binary search tree (balance BST)**. This arrangement is based on a normal BST, except that includes some additional restrictions in order to keep our O(log n) performance. Something that could diminish this efficiency would be having a considerable height difference between two subtrees. Balance BST algorithms are able to detect such differences and correct them. **AVL** and **Red Black trees** are self-balance BST that implement some of these algorithms. AVL trees don't allow a height difference greater than one between any of its subtrees nodes. With Red Black trees, each node carries an extra bit to keep track of its color, red or black. The root node and leaf nodes can only be black, and whenever there is a red node, both of its children must be black. Every path should include the same number of black nodes. For both BST, the algorithm rotates the nodes to follow these rules. Following these rules prevents them from losing their O(log n) performance. The following figures show both types of balanced BST and their respective operation.

<br>

![Figure 8](AVL_BBST.png)
<figcaption align = "center"><b>Figure 8 - AVL Balanced BST </b></figcaption>

<br>

<br>

![Figure 9](AVL_BBST_performance.png)
<figcaption align = "center"><b>Figure 9 - AVL Balanced BST Typical Operation </b></figcaption>

<br>

<br>

![Figure 10](Red_Black_BBST.png)
<figcaption align = "center"><b>Figure 10 - Red Black Balanced BST  </b></figcaption>

<br>

<br>

![Figure 11](Red_Black_BBST_performance.png)
<figcaption align = "center"><b>Figure 11 - Red Black Balanced BST Typical Operation </b></figcaption>

<br>

https://www.cs.usfca.edu/~galles/visualization/BST.html
https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

## How to Insert, Traverse and Access Data From a Tree

## Python Syntax

## Example

## Problem to Solve


[Back to Welcome Page](1-welcome.md)