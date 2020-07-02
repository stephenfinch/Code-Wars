def solution(string,markers):
	print(string)
	if not string:
		return ''
	if len(string) == 1:
		for mark in markers:
			if mark in string:
				return ''
	string = string.split('\n')
	for mark in markers:
		for i in range(len(string)):
			try:
				string[i] = string[i][:string[i].index(mark)-1]
			except:
				pass
	if '\n'.join(string) == '':
		return '\n'
	return '\n'.join(string).strip()




#solution("apples, pears #and bananas\ngrapes\nbananas !apples", ['!', '#'])
#print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), '\n\n-----------\n\n', "a\nc\nd")