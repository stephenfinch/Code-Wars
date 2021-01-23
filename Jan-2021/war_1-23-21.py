def nb_dig(n, d):
	nums = ''
	for k in range(1, n+1):
		nums += str(k**2)
	return nums.count(str(d))