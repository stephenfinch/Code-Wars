def parts_sums(ls):
	total = sum(ls)
	output = [total]
	for i in range(len(ls)):
		total -= ls[i]
		output.append(total)
	return output


def parts_sums(ls):
	output = [0]
	for i in range(len(ls) - 1, 0, -1):
		output.insert(0, ls[i] + output[0])
	output.insert(0, ls[0] + output[0])
	return output
