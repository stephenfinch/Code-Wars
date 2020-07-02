def validBraces(string):
	priority_chars = [''] # keep track of the most recent open braket
	brakets_to_close = 0
	table = {'(': ')', '{': '}', '[': ']'}
	for char in string:
		if char == table.get(priority_chars[-1]):
			brakets_to_close -= 1
			priority_chars = priority_chars[0:-1]
		elif char == '(' or char == '{' or char == '[':
			priority_chars.append(char)
			brakets_to_close += 1
	return brakets_to_close == 0

print(validBraces("[(])"))
print(validBraces("(){[(]"))
print(validBraces("([])"))
print(validBraces("[][]"))