rooms = {1:{'name': 0, 'description': 0, 'completed': 0}, 2:{'name': 0, 'description': 0, 'completed': 0}, 3:{'name': 0, 'description': 0, 'completed': 0}}

def capitalize_word(word):
	return word.title()

def ordered_count(s):
	output, seen = [], []
	for char in s:
		if char not in seen:
			output.append((char, s.count(char)))
		seen.append(char)
	return output

def remove_duplicate_ids(table):
	keys = sorted([int(n) for n in list(table.keys())])
	keys = [str(n) for n in keys]
	keys.reverse()
	print(keys)
	seen = []
	for k in keys:
		temp1, temp2 = table.get(k), []
		for i in temp1:
			if i not in seen:
				temp2.append(i)
			seen.append(i)
		table.update({k:temp2})
	keys.reverse()
	return {x:table.get(x) for x in keys}



b = {
    "1": ["C", "F", "G"],
    "2": ["A", "B", "C"],
    "3": ["A", "B", "D"],
}
res_b = {
    "1": ["F", "G"],
    "2": ["C"],
    "3": ["A", "B", "D"]
}
d = {
    "432": ["A", "A", "B", "D"],
    "53": ["L", "G", "B", "C"],
    "236": ["L", "A", "X", "G", "H", "X"],
    "11": ["P", "R", "S", "D"],
}
res_d = {
    "11": ["P", "R", "S"],
    "53": ["C"],
    "236": ["L", "X", "G", "H"],
    "432": ["A", "B", "D"]
}
print(remove_duplicate_ids(b), res_b)
print(remove_duplicate_ids(d), res_d)