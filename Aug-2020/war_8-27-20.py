def unique_in_order(i):
	output = [i[0]]
	for x in range(len(i)):
		if i[x] != output[-1]:
			output.append(i[x])
	return output