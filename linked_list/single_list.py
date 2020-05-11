class node:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next


class slist:
    def __init__(self):
        self.head = None


    def insert(self, data):
        newnode = node(data)

        if (self.head):
            cur_node = self.head
            while (cur_node.next):
                cur_node = cur_node.next
            cur_node.next = newnode
        else:
            self.head = newnode

    def display(self):
        if(self.head):
            cur_node = self.head
            
            while(cur_node):
                print(cur_node.data)
                cur_node = cur_node.next

        else:
            print("list is empty")
            

    def remove(self, data):

        cur_node = self.head
        prev_node = None

        if(not self.head):
            print("list is empty")

        else:
            while(cur_node and data != cur_node.data):
                prev_node = cur_node
                cur_node = cur_node.next

            if(cur_node is self.head):
                self.head = cur_node.next
            else:
                prev_node.next = cur_node.next
                

    def contains(self, data):
         if(not self.head):
            print("list is empty")

         else:
            cur_node = self.head
            
            while(cur_node and data != cur_node.data):
                cur_node = cur_node.next

            if (cur_node):
                print("found")
            else:
                print("not found")
                
           
          
                

lists = slist()
lists.insert(5)
lists.insert(4)
lists.insert(7)
lists.insert(0)
lists.insert(1)
lists.contains(5)
lists.display()
lists.remove(7)
lists.display()
            
