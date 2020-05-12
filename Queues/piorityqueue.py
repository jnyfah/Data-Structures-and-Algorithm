class entry(object):
	def __init__(self, item, piority):
		self.item = item
		self.piority = piority
class pqueue:
	def __init__(self):
		self.data =list()

	def isempty(self):
		return len(self.data)==0

	def length(self):
		return len(self.data)

	def enqueue(self, item, piority):
		newentry = entry(item, piority)
		self.data.append(newentry)

	def dequeue (self, item):

		assert not self.isempty(),  "queue is empty"
		highest = self.data[0].piority

		for i in range (len(self.data)):
			if self.data[i].piority<highest:
				highest = self.data[i].piority

		en = self.data.pop(highest)
		return en.item

			

st = pqueue()
st.enqueue(5,1)
x =st.dequeue(5)
		
