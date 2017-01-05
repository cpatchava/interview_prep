from tree import TreeNode
def main():
	a = TreeNode("a")
	c = TreeNode("c")
	e = TreeNode("e")
	h = TreeNode("h")
	i = TreeNode("i", h)
	g = TreeNode("g",None, i)
	d = TreeNode("d", c,e)
	b = TreeNode("b", a, d)
	f = TreeNode("f", b, g)
	print("in order")
	inOrder(f)	
	print("post order")
	postOrder(f)	
	print("pre order")
	preOrder(f)	

def levelOrder(curr):
	if curr != None:
		print(curr.val)
		levelOrder(curr.right)


def inOrder(curr):
	if curr != None:
		inOrder(curr.left)
		print (curr.val)
		inOrder(curr.right)

def postOrder(curr):
	if curr != None:
		postOrder(curr.left)
		postOrder(curr.right)
		print(curr.val)

def preOrder(curr):
	if curr != None:
		print(curr.val)
		postOrder(curr.left)
		postOrder(curr.right)


if __name__ == '__main__':
	main()
