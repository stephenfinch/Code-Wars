def yes_no(arr):
	output = []
	for i in range(len(arr)):
		print(arr, output)
		if i % 2 == 0:
			a = i % len(arr)
			output.append(arr.pop(a))
	return output



print(yes_no(['this', 'code', 'is', 'right', 'the']))