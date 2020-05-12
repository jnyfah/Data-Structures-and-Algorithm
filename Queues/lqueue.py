class node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class queue:
    def __init__(self):
        self.head = None
        self.count =0


    def isempty(self):
        if(not self.head):
            status = True
        else:
            status =False
        return status

    def length(self):
        return self.count

    def enqueue(self, data):
        newnode = node(data)
        if(self.isempty):
            self.head = newnode
        else:
            curnode = self.head
            while (curnode):
                curnode = curnode.next
            curnode.next =newnode
        self.count +=1



    def dequeue(self):
        assert not self.isempty(), "stack is empty"
        
        self.head = self.head.next 
        self.count -=1

    def display(self):
        if(not self.head):
            print("queue is empty")
        else:
            curnode = self.head
            while (curnode):
                print(curnode.data)
                curnode = curnode.next
            





st = queue()
st.enqueue(7)
st.enqueue(6)
st.enqueue(6)
st.enqueue(6)

st.display()
