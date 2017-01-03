import sys
def fizzbuzz():
	for i in range (0, 101):
		if i % 3 is 0:
			sys.stdout.write("fizz")
		if i%5 is 0:
			sys.stdout.write("buzz")
		sys.stdout.write("\n")
		if i%5 is not 0 and i%3 is not 0:
			sys.stdout.write(str(i))
fizzbuzz()	
