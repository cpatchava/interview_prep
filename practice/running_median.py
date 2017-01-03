#we are going to have a max heap of low vals and min heap of max vals
#we will push and pop and keep our running median that way, if the trees are not
#even we adjust
import heapq

class Heap():
	
	def __init__(self, max_or_min=0):
		self.h=[]
		self.min_heap = max_or_min
	
	def push(self, val):
		if not self.min_heap:
			heapq.heappush(self.h, val)
		if self.min_heap:
			val = int(val)*-1
			heapq.heappush(self.h, val)

	def pop(self):
		if not self.min_heap:
			return heapq.heappop(self.h)
		if self.min_heap:
			ret = int(heapq.heappop(self.h)) * -1
			return ret

	def size(self):
		return len(self.h)

def running_median():
	myNums=[10,30,5,6,9,13,55,300,1,2,3,7000, 70001]#if numbers is even, median will be larger #
	minHeap = Heap(0) #contains biggest numbers
	maxHeap = Heap(1) #contains smallest numbers
	currMedian = myNums[0]
	for x in range(1, len(myNums)):
		#heaps are both empty and our initial value is our median
		print (str(currMedian) +" " + str(myNums[x]))
		if currMedian < myNums[x]:
			minHeap.push(myNums[x])
		else:
			maxHeap.push(myNums[x])

		diff = int(minHeap.size()) - int(maxHeap.size())
		if diff < 0:
			minHeap.push(currMedian)
			currMedian = maxHeap.pop()
		elif diff > 0:
			maxHeap.push(currMedian)
			currMedian = minHeap.pop()

running_median()
