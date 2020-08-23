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

def solve(a):
	'''
	if the count of the number to your left is less than you switch
	if that count is equal and that number is bigger than you switch
	loop backwards through the arr
	restart ever time you switch
	'''
	loop, end_loop = True, False
	while loop:
		temp = a.slice()
		if end_loop: loop = False
		for i in range(len(a)-1,1,-1):
			if a.count(a[i-1]) < a.count(a[i]):
				a = swap(a, i-1, i)
				break
			elif (a.count(a[i-1]) == a.count(a[i])) and a[i-1] > a[i]:
				a = swap(a, i-1, i)
				break
			#a == temp: end_loop = True
	return a

def swap(a, h, k):
	a[h], a[k] = a[k], a[h]
	return a

p = [1, 1, 1, 0, 0, 6, 8, 8, 6, 2, 3, 5, 9]
#print(solve([1,2,3,0,5,0,1,6,8,8,6,9,1]),[1,1,1,0,0,6,6,8,8,2,3,5,9])
#print(solve(p),[1,1,1,0,0,6,6,8,8,2,3,5,9])


print([1,4] == [1,4])