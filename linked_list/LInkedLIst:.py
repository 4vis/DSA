class Linkedlist:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
        self.currsize = 0
        
    #displaying the linked list
    
    def display(self):
        curr_node = self.head
        if curr_node is not None:
            while curr_node:
                print(curr_node.data  + " -> ")
                curr_node = curr_node.next
            return
        
        print("Empty linked list")
        
        
            
            