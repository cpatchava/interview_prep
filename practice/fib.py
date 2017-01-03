def fib(n):
	prev = 0
	curr = 1
	for x in range(1, n):
		ret = curr + prev
		prev = curr
		curr = ret
	print ret

def fib_r(n, computed={0:0, 1:1}):
	if n in computed:
		return computed[n]
	else:
		computed[n] = fib_r(n-1, computed) + fib_r(n-2,computed)

fib_r(8)
