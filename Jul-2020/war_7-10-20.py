def persistence(n):
	i = 0
	while len(str(n)) > 1:
		num = 1
		for diget in str(n):
			num *= int(diget)
		n = num
		i += 1
	return i

print(persistence(39), 3)