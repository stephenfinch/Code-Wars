'''
def summation(num):
	return sum(range(1,num+1))

def solve(s):
	if test(s):
		return 'OK'
	for i in range(len(s)):
		temp = s[:i]+s[i+1:]
		if test(temp):
			return 'remove one'
	return 'not possible'

def test(s):
	output = True
	for i in range(len(s)):
		if s[i] != s[-1-i]:
			output = False
	return output
'''

def solve(a):
	values, output, set_ = [], [], list(set(a))
	set_.sort()
	for i in range(len(set_)):
		values.append([a.count(set_[i]),-set_[i],])
	values.sort()
	values.reverse()
	for item in values:
		for j in range(item[0]):
			output.append(item[1]*-1)
	return output



p = [1, 1, 1, 0, 0, 6, 8, 8, 6, 2, 3, 5, 9]
print(solve([1,2,3,0,5,0,1,6,8,8,6,9,1]),[1,1,1,0,0,6,6,8,8,2,3,5,9])
#print(solve(p),[1,1,1,0,0,6,6,8,8,2,3,5,9])