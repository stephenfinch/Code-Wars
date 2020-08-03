'''
def solve(s):
	spaces = []
	for i in range(len(s)):
		if s[i] == ' ':
			spaces.append(i)
	s = s.replace(' ', '')
	s = list(s)
	s.reverse()
	for space in spaces:
		s.insert(space, ' ')
	return ''.join(s)


print(solve("i love codewars"),"s rawe docevoli")
'''


def solve(s,a,b):
	return s[:a] + s[a:b+1][::-1] + s[b+1:]


print(solve("codewars",1,5),"cawedors")
print(solve("codingIsFun",2,100),"conuFsIgnid")

from itertools import product 
def solve(arr):
	return max(product(arr[0], arr[1]))