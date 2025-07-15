class Linkedlist:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
        self.currsize = 0
        self.tail = None
    
    #isempty method for ease of use
    def isempty(self):
        if self.currsize == 0:
            return True
        else:
            return False
      
    #displaying the linked list
    def display(self):
        if self.isempty():
            print("Lock in bro")
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.data, end=" -> ")
                curr_node = curr_node.next
        print("\nll size: ",self.currsize)

    def addfirst(self,data):
        node = self.Node(data)
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            tmpvar = self.head
            self.head = node
            self.head.next = tmpvar  
        self.currsize+=1
        
    def addlast(self, data):
        if self.isempty():
            self.addfirst(data)
        else:
            node = self.Node(data)
            self.tail.next = node
            self.tail = node
            self.currsize+=1
        
        
            
            