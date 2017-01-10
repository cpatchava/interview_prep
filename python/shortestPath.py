saved = {}
def path(n):
	if n in saved:
		return saved[n]
	elif n == 2:
		return 1
	elif not n%2:
		saved [n] = 1 + path(n/2)
		return saved[n]
	else:
		add = 1 + path(n+1)
		sub = 1 + path(n-1)
		if add > sub:
			saved[n] = sub
		else:
			saved[n] = add
		return saved[n]


print(path(100000000))
