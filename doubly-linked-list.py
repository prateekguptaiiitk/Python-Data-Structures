class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:

  def __init__(self):
    self.head = None

  def insertFront(self, new_data):
    new_node = Node(new_data)

    new_node.next = self.head

    if self.head is not None:
      self.head.prev = new_node

    self.head = new_node

  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("the given previous node cannot be NULL")
      return

    new_node = Node(new_data)

    new_node.next = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node

    if new_node.next:
      new_node.next.prev = new_node

  def insertEnd(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node
    new_node.prev = last

    return

  def printList(self, node):
    print("\nTraversal in forward direction")
    while node:
      print("{}".format(node.data), end =" ")
      last = node
      node = node.next

    print("\nTraversal in reverse direction")
    while last:
      print("{}".format(last.data), end =" ")
      last = last.prev
    print()

  def deleteNode(self, head, delete):
    if (head == None or delete == None):
      return None
 
    if (head == delete):
      head = delete.next
 
    if (delete.next != None):
      delete.next.prev = delete.prev
 
    if (delete.prev != None):
      delete.prev.next = delete.next
 
    delete = None
    return head
 
  def deleteAllOccurOfX(self, head, x):
    if (head == None):
        return
 
    current = head
 
    while (current != None):
      if (current.data == x):
        next = current.next
        head = self.deleteNode(head, current)
        current = next
      else:
        current = current.next
     
    return head
 
if __name__ == "__main__":
  llist = DoublyLinkedList()

  llist.insertEnd(6)

  llist.insertFront(7)

  llist.insertFront(1)

  llist.insertEnd(4)

  llist.insertAfter(llist.head.next, 8)

  print("Created DLL is: ", end =" ")
  llist.printList(llist.head)

  head = llist.deleteAllOccurOfX(llist.head, 7)

  print("After deletion DLL is: ", end =" ")
  llist.printList(head)
