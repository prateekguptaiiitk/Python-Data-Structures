class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # print linked list
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  #insert new node at beginning
  def insertBeginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  #insert new node after a node
  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print('Previous node does not exist')
      return

    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  #insert new node at the end
  def insertEnd(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node

  def searchIterative(self, key):
 
    current = self.head
 
    while current != None:
      if current.data == key:
        return True
 
      current = current.next
 
    return False  
 
  def searchRecursive(self, head, key):
 
    if not head:
      return False
 
    if head.data == key:
      return True

    return self.searchRecursive(head.next, key)

  def reverseIterative(self):
    prev = None
    current = self.head
        
    while(current is not None):
      temp = current.next
      current.next = prev
      prev = current
      current = temp
      self.head = prev

  def reverseRecursive(self, head):
    if head is None or head.next is None:
      return head
 
    rest = self.reverseRecursive(head.next)
 
    head.next.next = head
    head.next = None
 
    return rest

  def reverseUtil(self, curr, prev):
    if curr.next is None:
      self.head = curr
      curr.next = prev
      return
 
    next = curr.next
    curr.next = prev
    self.reverseUtil(next, curr)
 
  def reverseTailRecursive(self):
    if self.head is None:
      return
    self.reverseUtil(self.head, None)

  def reverseLLUsingStack(self, head):
    stack, temp = [], head
 
    while temp:
      stack.append(temp)
      temp = temp.next
 
    head = temp = stack.pop()
 
    while len(stack) > 0:
      temp.next = stack.pop()
      temp = temp.next
 
    temp.next = None
    return head
 
  def deleteIterative(self, key):
    temp = self.head

    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        return

    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next

    if temp == None:
      print('Element not found')
      return

    prev.next = temp.next
    temp = None

  def deleteRecursive(self, head, val):
    if (head == None):
      print("Element not present in the list")
      return -1
    
    if (head.data == val):
      if head.next:
        head.data = head.next.data
        head.next = head.next.next
        return 1
      else:
        return 0

    if self.deleteRecursive(head.next, val) == 0:
      head.next = None
      return 1

  def deleteNodeAtGivenPosition(self, position):
    if self.head is None:
      return
    
    index = 0
    current = self.head
        
    while current.next and index < position:
      previous = current
      current = current.next
      index += 1
        
    if index < position:
      print("Index is out of range.")
    elif index == 0:
      self.head = self.head.next
    else:
      previous.next = current.next
    
if __name__ == '__main__':

  llist = LinkedList()
  llist.insertEnd(6)
  llist.insertBeginning(7)
  llist.insertBeginning(1)
  llist.insertEnd(4)
  llist.insertAfter(llist.head.next, 8)

  print('created linked list:')
  llist.printList()

  if llist.searchIterative(4):
    print("found 4")
  else:
    print('not found 4')

  if llist.searchRecursive(llist.head, 94):
    print('found 94')
  else:
    print('not found 94')

  llist.deleteIterative(1)
  print('linked list after deleting 1')
  llist.printList()

  llist.deleteIterative(8)
  print('linked list after deleting 8')
  llist.printList()

  llist.deleteRecursive(llist.head, 4)
  print('linked list after deleting 4 recursively')
  llist.printList()

  print('trying to delete 1')
  llist.deleteIterative(1)
  llist.printList()

  print("Linked List after Deletion at index 3: ")
  llist.deleteNodeAtGivenPosition(3)
  llist.printList()

  llist.reverseIterative()
  print ("Iteratively reversed linked list")
  llist.printList()

  head = llist.reverseRecursive(llist.head)
  print ("Recursively reversed linked list")
  while head:
    print(head.data, end=' ')
    head = head.next
    print()

  llist.reverseTailRecursive()
  print("Tail Recursively reversed linked list")
  llist.printList()

  print('Reversed linked list using stack')
  head = llist.reverseLLUsingStack(llist.head)
  while head:
    print(head.data, end=' ')
    head = head.next
    print()
