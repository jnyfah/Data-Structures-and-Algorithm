class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if (not self.head):
            status = True
        else:
            status = False
        return status

    def push(self, data):
        newnode = node(data)

        if(self.isempty()):
            self.head = newnode

        else:
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        assert self.isempty(),  "cannot pop empty stack"
        temp = self.head
        self.head = self.heah.next
        print(temp)


x = stack()
x.push(3)
x.push(2)
