def main():
	print ("inside main")
	node = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	print(node)

class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next
	
	def __str__(self):
		return str(self.val)


if __name__ == '__main__':
	main()
