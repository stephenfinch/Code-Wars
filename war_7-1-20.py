def yes_no(arr):
	new_list = arr[:]

	while len(arr) > 2:
		pops = []
		for i in range(1, len(arr), 2):
			new_list.append(arr[i])
		for x in range(0, len(arr), 2):
			pops.append(x)
		pops.reverse()
		for a in pops:
			arr.pop(a)
	output = []
	for i in range(0, len(new_list), 2):
		output.append(new_list[i])

	return output+[arr[0]]





print(yes_no(['this', 'code', 'is', 'right', 'the']))

lst = ['this', 'code', 'is', 'right', 'the'] + ['code', 'right'] + ['code']
print(lst)