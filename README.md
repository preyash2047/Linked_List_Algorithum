Linked_List_Algorithum By Preyash Patel

<h>

Introduction

Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

Why Linked List?  

Arrays can be used to store linear data of similar types, but arrays have the following limitations.  

1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.  

2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create a room existing elements have to be shifted.  

For example, in a system, if we maintain a sorted list of IDs in an array id[].  

id[] = [1000, 1010, 1050, 2000, 2040].  

And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000).  

Deletion is also expensive with arrays unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved.

Advantages over arrays  

1) Dynamic size  

2) Ease of insertion/deletion

Drawbacks:  

1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists efficiently with its default implementation. Read about it here.  

2) Extra memory space for a pointer is required with each element of the list.  

3) Not cache-friendly. Since array elements are contiguous locations, there is the locality of reference which is not there in the case of linked lists.

Representation:  

A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.  

Each node in a list consists of at least two parts:  

1) data  

2) Pointer (Or Reference) to the next node  

Python3

class Node:
  def __init__(self,data):
    self.data = {
        "data" : data,
        "next_node" : None
    }

class LinkedList:
  def __init__(self, element):
    #initalizing the linked list
    self.hadeNode = Node("head")

    #appending the first node
    obj = Node(element)
    self.hadeNode.data["next_node"] = Node(element)
    self.node = self.hadeNode
    self.node.data["next_node"] = obj

    #setting the default node for further operation
    self.node = obj

  def addNode(self, element):
    obj = Node(element)
    self.node.data["next_node"] = obj
    self.node = obj

  def printLL(self):
    current = self.hadeNode
    while(current):
      print(current.data["data"])
      current = current.data["next_node"]

obj = LinkedList(1)
for i in range(2,10):
  obj.addNode(f"I am Node Data {i}")
obj.printLL()

