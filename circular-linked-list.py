class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def push(self, data):
    newP = Node(data)
    newP.next = self.head
  
    if self.head != None:
      temp = self.head
      while (temp.next != self.head):
        temp = temp.next
      temp.next = newP
    else:
      newP.next = newP

    self.head = newP

  def printList(self):
    if self.head == None:
      print("List is Empty")
      return

    temp = self.head.next
    print(self.head.data,end=' ')

    if (self.head != None):
      while (temp != self.head):
        print(temp.data, end=" ")
        temp = temp.next
    print()

  def deleteNode(self, key):
    if (self.head == None):
      return

    if (self.head.data == key and self.head.next == self.head):
      head = None
      return
  
    last = self.head

    if (self.head.data == key):
      while (last.next != self.head):
        last = last.next

      last.next = self.head.next
      self.head = last.next
      return

    while (last.next != self.head and last.next.data != key):
      last = last.next

    if (last.next.data == key):
      d = last.next
      last.next = d.next
      d = None
    else:
      print("Given node is not found in the list!!!")

if __name__ == '__main__':
  clist = CircularLinkedList()

  clist.push(2)
  clist.push(5)
  clist.push(7)
  clist.push(8)
  clist.push(10)

  print("List Before Deletion: ")
  clist.printList()

  clist.deleteNode(7)
  print("List After Deletion: ")
  clist.printList()
