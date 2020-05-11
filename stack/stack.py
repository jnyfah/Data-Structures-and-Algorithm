class stack:
    def __init__(self):
        self.data = list()

    def isempty(self):
        return len(self.data) 

    def pop(self):
        assert self.isempty(), "stack is empty"
        print(self.data.pop())
        return self.data.pop()
    

    def push (self, item):
        self.data.append(item)

def main():

    x = stack()
    x.push(9)
    x.push(8)
    x.pop()
    

main()
