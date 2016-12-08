#
#an array s of N ints
#find a+b+c = 0 all unq sets
#

"""
def findSets(myArr):
	print(myArr)
	first=1
	second=0
	d = {}
	for n in myArr:
		for x in range (n+1, len(myArr)):
			d[int(myArr[x]) + int(myArr[n])] = str(myArr[x]) + " " + str(myArr[n])
	for n in myArr :
		idx = int(myArr[n])*-1
		if d[idx]:
			print d[int(myArr[n])] + " " + str(myArr[n])
"""



def findSets(myArr):
	myArr.sort()
	print myArr
	arrLen = len(myArr) -1
	delete=0
	for n in range(0, arrLen):
		if n >arrLen:
			break
		lowestVal=myArr[n]
		for m in range(1 + n, arrLen):
			if m>arrLen:
				break
			secondVal=myArr[m]
			findVal=int(lowestVal)+int(secondVal)
			for o in range(arrLen, m, -1):
				if abs(findVal) < myArr[o]:
					myArr.pop()
					o=o-1
					arrLen=arrLen-1
				elif abs(findVal) == int(myArr[o]):
					print str(lowestVal) + " " + str(secondVal) + " " + str(myArr[o])
					myArr.pop()
					o=o-1
					arrLen=arrLen-1
				else:
					break
		
			

"""
def findSets(myArr):
	for n in range(0, len(myArr)):
		if int(myArr[n]) < 0 :
			for m in range(0, len(myArr)):#neg number
				if m == n:
					continue
				curr_lookup=-1*(myArr[n] + myArr[m])
				for o in range(0,len( myArr)):
					if o==m or o==n:
						continue
					if myArr[o] == curr_lookup:
						print str(myArr[n]) + " " + str(myArr[m]) + " " + str(myArr[o])
	"""	
def main():
	myArr = [-1, 0,2,-1,1,-4, -4,-4,-1,-1, 4, 2, 2,2]
	findSets(myArr)
#	print myArr[0]

if __name__ == '__main__':
	main()
