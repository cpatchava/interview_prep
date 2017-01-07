from tree import TreeNode
from collections import deque

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
	print("level order")
	sibling(f)
	print("sibling order")
	levelOrderPrint(f)
		

def levelOrderPrint(curr):
	q = deque([])
	q.append(curr)
	while len(q):
		curr = q.popleft()
		print(str(curr.val) )
		if curr.sibling:
			print ("sibling " + str(curr.sibling.val))
		if curr.right:
			q.append(curr.right)
		if curr.left:
			q.append(curr.left)

	
def sibling(curr):
	q = deque([])
	q.append(curr)
	curr_last = curr
	while len(q):
		curr = q.popleft()
		print(curr.val)

		if curr.left:
			curr_val = curr.left
			q.append(curr_val)
		if curr.right:
			curr_val = curr.right
			q.append(curr_val)

		if curr == curr_last:
			curr_last = None
			if len(q) :
				for x in range(0, len(q)-1):
					q[x].sibling = q[x+1]

		if curr_last is None:
			curr_last = curr_val


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
