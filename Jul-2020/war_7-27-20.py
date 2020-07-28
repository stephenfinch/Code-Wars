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
	keys = sorted(list(table.keys()))
	keys.reverse()
	seen = []
	for k in keys:
		temp1, temp2 = set(table.get(k)), []
		for i in temp1:
			if i not in seen:
				temp2.append(i)
			seen.append(i)
		temp2.reverse()
		table.update({k:temp2})
	return table



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
print(remove_duplicate_ids(b), res_b)