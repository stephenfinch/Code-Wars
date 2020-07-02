def anagrams(word, words):
	output = []
	first = {}
	word = list(word)
	for char in word:
		first.update({char:word.count(char)})
	for w in words:
		test = {}
		w = list(w)
		for char in w:
			test.update({char:w.count(char)})
		if test == first:
			output.append(''.join(w))
	return output

#print(anagrams('codeeoe', ['hey', 'they', 'codeeoe', 'codeeeo', 'deeoeco']))


def sum_of_intervals(items):
	small, big, lst = [], [], []
	for item in items:
		small.append(item[0])
		big.append((item[1]))
	for item in items:
		for i in range(min(small),max(big)):
			if i in range(item[0],item[1]):
				if i in lst:
					pass
				else:
					lst.append(i)
	return len(lst)

lst1 = [[1,5],[2,12],[7,9],[1,2],[2,9],[18,21]]
#print(sum_of_intervals(lst1))
#print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
#print(sum_of_intervals([[1, 5]]), 4)

