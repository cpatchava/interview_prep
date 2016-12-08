def main():
	print("inside main")
	root = TreeNode(2)
	root.insertNode(10, root)
	root.insertNode(9, root)
	root.insertNode(13, root)
	root.insertNode(1, root)
	root.insertNode(5, root)
	root.insertNode(30, root)
#	root.printTree()
	print(root.right.countNodes())	
class TreeNode:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	
	def __str__(self):
		return str(self.val)

	def insertNode(self, val, root):
		if self.val < val:
			if self.right == None:
				self.right = TreeNode(val, root)
			else:
				self.right.insertNode(val, root)
		else:
			if self.left == None:
				self.left = TreeNode(val, root)
			else:
				self.left.insertNode(val, root)
		self.balanceTree(root)
		
	def balanceTree(self, root):
		left_size=0
		right_size=0
		if root.left is not None:
			left_size=root.left.countNodes()
		if root.right is not None:
			right_size=root.right.countNodes()
	
	def countNodes(self):
		count=1
		if self.left is not None:
			count += self.left.countNodes()
		if self.right is not None:
			count += self.right.countNodes()
		return count

	def printTree(self):
		print(self)
		if self.left != None:
			self.left.printTree()
		if self.right != None:
			self.right.printTree()

if __name__ == '__main__':
	main()
