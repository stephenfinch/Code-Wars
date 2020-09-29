def pairs(a):
	sets, count = [(a[i], a[i+1]) for i in range(0, len(a)-1, 2)], 0
	for item in sets:
		if item[0] <= item[1]:
			count += 1
	return count
	


print(pairs([1,2,5,8,-4,-3,7,6,5]),3)