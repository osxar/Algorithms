<<<<<<< HEAD

class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):

        if(index<0 or index>self.size-1):
            return -1

        currentNode = self.head

        while(index!=0):
            currentNode = currentNode.next
            index-=1

        return currentNode.val

    def addAtHead(self,val):

        newHead = Node(val)

        if (self.head is None): 
            self.head = newHead
            self.tail = newHead
        else:
            oldHead = self.head
            
            oldHead.prev = newHead
            newHead.next = oldHead
            self.head = newHead
        
        self.size+=1  

    def addAtTail(self,val):
        newTail = Node(val)

        if (self.tail is None):
            self.tail = newTail
            self.head = newTail
        else:
            oldtail = self.tail
            oldtail.next = newTail
            newTail.prev = oldtail
            self.tail = newTail

        self.size+=1

    def addAtIndex(self,index,val):
        
        if(index<0 or index>self.size):
            return -1
       

        if(index == 0):
            self.addAtHead(val)
        elif(index == self.size):
            self.addAtTail(val)
        else:
            newNode = Node(val)
            currentValue = self.head
            index-=1 

            while(index!=0):
                currentValue = currentValue.next
                index-=1

            nextValue = currentValue.next

            currentValue.next = newNode
            newNode.prev = currentValue

            newNode.next = nextValue
            nextValue.prev = newNode

            self.size+=1
    
    def deleteAtIndex(self,index):
        
        if(index<0 or index>self.size-1):
            return -1

        if(self.size==1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            currentvalue = None

            if(index==0):
                currentValue = self.head
                newvalue = currentValue.next
                newvalue.prev = None

                currentValue.next = None
                self.head = newvalue
                self.size-=1

                if(self.size==1):
                    self.tail = newvalue
                            
            elif(index==self.size-1):
                currentValue = self.tail 
                newvalue = currentValue.prev

                newvalue.next = None
                currentValue.prev = None
                
                self.tail = newvalue
                self.size-=1

                if(self.size==1):
                    self.head = newvalue                      
            else:
                index-=1

                currentNode = self.head

                while(index!=0):
                    currentNode = currentNode.next
                    index-=1
                
                delNode = currentNode.next
                nextNode = currentNode.next.next

                currentNode.next = nextNode
                nextNode.prev = currentNode

                delNode.next = None
                delNode.prev = None
               

                self.size-=1

def printLL(a):
    curr = a.head
    while(curr.next != None):
        print(curr.val)
        curr = curr.next
    print(curr.val)


obj = LinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)

printLL(obj)

# Expected Output
# 6->4->6->1->2->0->0->4
=======

class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):

        if(index<0 or index>self.size-1):
            return -1

        currentNode = self.head

        while(index!=0):
            currentNode = currentNode.next
            index-=1

        return currentNode.val

    def addAtHead(self,val):

        newHead = Node(val)

        if (self.head is None): 
            self.head = newHead
            self.tail = newHead
        else:
            oldHead = self.head
            
            oldHead.prev = newHead
            newHead.next = oldHead
            self.head = newHead
        
        self.size+=1  

    def addAtTail(self,val):
        newTail = Node(val)

        if (self.tail is None):
            self.tail = newTail
            self.head = newTail
        else:
            oldtail = self.tail
            oldtail.next = newTail
            newTail.prev = oldtail
            self.tail = newTail

        self.size+=1

    def addAtIndex(self,index,val):
        
        if(index<0 or index>self.size):
            return -1
       

        if(index == 0):
            self.addAtHead(val)
        elif(index == self.size):
            self.addAtTail(val)
        else:
            newNode = Node(val)
            currentValue = self.head
            index-=1 

            while(index!=0):
                currentValue = currentValue.next
                index-=1

            nextValue = currentValue.next

            currentValue.next = newNode
            newNode.prev = currentValue

            newNode.next = nextValue
            nextValue.prev = newNode

            self.size+=1
    
    def deleteAtIndex(self,index):
        
        if(index<0 or index>self.size-1):
            return -1

        if(self.size==1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            currentvalue = None

            if(index==0):
                currentValue = self.head
                newvalue = currentValue.next
                newvalue.prev = None

                currentValue.next = None
                self.head = newvalue
                self.size-=1

                if(self.size==1):
                    self.tail = newvalue
                            
            elif(index==self.size-1):
                currentValue = self.tail 
                newvalue = currentValue.prev

                newvalue.next = None
                currentValue.prev = None
                
                self.tail = newvalue
                self.size-=1

                if(self.size==1):
                    self.head = newvalue                      
            else:
                index-=1

                currentNode = self.head

                while(index!=0):
                    currentNode = currentNode.next
                    index-=1
                
                delNode = currentNode.next
                nextNode = currentNode.next.next

                currentNode.next = nextNode
                nextNode.prev = currentNode

                delNode.next = None
                delNode.prev = None
               

                self.size-=1

def printLL(a):
    curr = a.head
    while(curr.next != None):
        print(curr.val)
        curr = curr.next
    print(curr.val)


obj = LinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)

printLL(obj)

# Expected Output
# 6->4->6->1->2->0->0->4
>>>>>>> f277f8473d0fccc67fc3a250410e724227ed3796
