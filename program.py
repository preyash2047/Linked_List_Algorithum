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