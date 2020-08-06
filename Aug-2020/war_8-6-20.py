def parts_sums(ls):
	return [sum(ls)] + [sum(ls)-ls.pop(0) for x in range(len(ls))]