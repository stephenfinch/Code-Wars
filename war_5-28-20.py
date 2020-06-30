"""
def solution(s):
	lst = []
	for i in range(len(s)):
		item = s[i]
		if i % 2 == 0:
			try:
				item += s[i+1]
			except:
				item += '_'
			lst.append(item)
	return lst

print(solution('abc'), '''['ab', 'c_']''')
print(solution('abcdef'), '''['ab', 'cd', 'ef']''')
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution("x"), ['x_'])
"""


def digital_root(n):
	while len(str(n)) > 1:
		num = []
		for x in range(len(str(n))):
			num.append(int(str(n)[x]))
		n = sum(num)
	return n

print(digital_root(16), 7)
print(digital_root(136), 1)
print(digital_root(112346), 8)
print(digital_root(493193), 2)
print(digital_root(132189), 6)


def find_it(seq):
	for item in seq:
		if seq.count(item) % 2 != 0:
			return item