def yes_no(arr):
	output = []
	new_arr = arr*3
	i = 0
	while len(new_arr) > 1:

		if i % 2 == 0:
			output.append(new_arr[0])
			new_arr = [x for x in new_arr if x != output[-1]]
		else:
			new_arr = new_arr[1:]
		i += 1
	return output+new_arr




print(yes_no(['this', 'code', 'is', 'right', 'the']))

lst = ['this', 'code', 'is', 'right', 'the'] + ['code', 'right'] + ['code']
lst1 = ['this', 'code', 'is', 'right', 'the']

