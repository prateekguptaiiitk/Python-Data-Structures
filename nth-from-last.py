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

  def insertEnd(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node

  def printNthFromLastNaive(self, n):
    temp = self.head
  
    length = 0
    while temp is not None:
      temp = temp.next
      length += 1
  
    if n > length:  
      print('Location is greater than the' + ' length of LinkedList')
      return
        
    temp = self.head
    for i in range(0, length - n):
      temp = temp.next
    print(temp.data, " is node ", n, "from last")
  

  def printNthFromLast(self, N):
    main_ptr = self.head
    ref_ptr = self.head
  
    count = 0
    if(self.head is not None):
      while(count < N):
        if(ref_ptr is None):
          print("% d is greater than the no. of nodes in list" % (N))
          return
        ref_ptr = ref_ptr.next
        count += 1
  
    if(ref_ptr is None):
      self.head = self.head.next
      if(self.head is not None):
        print("Node no. % d from last is % d " % (N, main_ptr.data))
    else:
      while(ref_ptr is not None):
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
      
      print("Node no. % d from last is % d "
                  % (N, main_ptr.data))
    
if __name__ == '__main__':

  llist = LinkedList()
  llist.insertEnd(6)
  llist.insertEnd(7)
  llist.insertEnd(1)
  llist.insertEnd(4)
  llist.insertEnd(8)

  print('created linked list')
  llist.printList()

  llist.printNthFromLast(4)
  llist.printNthFromLastNaive(2)
