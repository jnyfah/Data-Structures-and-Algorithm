class queue:
    def __init__(self):
        self.data = list()


    def isempty(self):
        return self.data ==0

    def length(self):
        return len(self.data)a

    def enqueue(self, data):
        self.data.append(data);

    def dequeue(self):
        assert not self.isempty(), "stack is empty"
        return self.data.pop(0)



st = queue()
st.enqueue(7)

print(st.dequeue())
