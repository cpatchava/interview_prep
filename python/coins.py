"""def findPossibleSum(coin_arr, total):
	size = total
	my_list = [None]*total
	for x in range(0, total):
		
def findCombos(x, coin_arr, curr_list):
	if x == 0:
		return 0
	else:
		
"""






def findSum(coin_arr, total):
	dynamicArr = {}
	for x in range(0, total):
		dynamicArr[x] = []
		my_helper(total, coin_arr, x )
			

def my_helper(total, coin_arr, start):
	for x in range (start, len(coin_arr)):
		if total - coin_arr[x] > 0:
			print my_helper(total - coin_arr[x], coin_arr, start)
		elif total - coin_arr[x] is 0:
			return coin_arr[x]
		else:
			print ""	
findSum([1,2,3], 5)
