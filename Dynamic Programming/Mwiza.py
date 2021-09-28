# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
	def __init__(self, array):
		# Do not edit the line below.
		self.heap = self.buildHeap(array)

	def buildHeap(self, array):
		# Write your code here.
		for item in array:
			self.heap.append(item)
			self.siftUp(len(self.heap)-1)
		return array
	def siftDown(self, index= None):
		# Write your code here.
		left = index * 2
		right = (index * 2) +1
		largest = index
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if largest != index:
			self.swap(largest, index)
			self.siftDown(largest)

	def siftUp(self, index= None):
		# Write your code here.
		parent = index // 2
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.swap(index, parent)
			self.siftUp(parent)

	def peek(self):
		# Write your code here.
		if self.heap[1]:
			return self.heap[1]
		else:
			False

	def remove(self):
		# Write your code here.
		if len(self.heap) > 2:
			self.swap(1, len(self.heap)-1)
			max = self.heap.pop()
			self.siftDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			return False
		return max

	def insert(self, value):
		# Write your code here.
		self.heap.append(value)
		self.siftUp(self, len(array)-1)
	
	def swap(self, start, end):
		self.heap[start], self.heap[end] = self.heap[end], self.heap[start]