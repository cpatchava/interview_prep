
saved = {}

def findSum(coins, total):
	for x in range (coins[0], total):
		my_helper(coins, x)
	print saved

def my_helper(coins, curr_total):
	if curr_total in saved:
		return str(saved[curr_total])
	elif curr_total < coins[0]:
		return
	else:
		for x in range(0, len(coins)):
			lists = []
			my_str = str(coins[x]) + " " + str(findSum(coins, curr_total - coins[x]))
			lists.append(my_str)
			saved[curr_total] = lists
			return my_str
findSum([1,2,3], 5)
