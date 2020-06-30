import math

def format_duration(s):
	m = math.floor(s/60)
	h = math.floor(m/60)
	d = math.floor(h/24)
	y = math.floor(d/365)
	s = s%60
	m = m%60
	h = h%24
	d = d%365

	results = [y,d,h,m,s]
	times = ['year', 'day', 'hour', 'minute', 'second']
	output = []

	for i in range(len(times)):
		if results[i] == 0:
			pass
		elif results[i] == 1:
			output.append(str(results[i])+' '+times[i])
		else:
			output.append(str(results[i])+' '+times[i]+'s')

	if len(output) > 2:
		return ', '.join(output[:-1])+' and '+output[-1]
	elif len(output) == 2:
		return output[0]+' and '+output[1]
	elif len(output) == 1:
		return output[0]
	else:
		return 'now'
#print(format_duration(15731080))
#print(format_duration(1))

lst = [4, -11, 28, 0, -16, 14, -11, -16, -23, -1, -1, 10, -7, 5, 30, -10, 1, 11, 18, -15, -4, -7, 24, 29, -30, -19, 22, -30, -16, -15, -10, 26, 0, -11, 16, 27, 23, 10, -3, 12, 20, -21, -29, -15, -12, -6, -4, 15, -29, -27]
lst1 = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
lst2 = [5,5,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,5,5,-9,-9,-9,-9,5,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9]

'''
def max_sequence(arr):
	#print(arr)
	count = 0
	for item in arr:
		if item < 0:
			count += 1
		if count == len(arr):
			return 0
	for i in range(len(arr)): #could make this faster
		print(arr)
		if arr[0] <= 0:
			arr = arr[1:]
		elif sum(arr[0:2]) <= 0:
			arr = arr[2:]
		if arr[-1] <= 0:
			arr = arr[0:-1]
		elif sum(arr[-2:]) <= 0:
			arr = arr[0:-2]

	return arr


def max_sequence(arr):
	current_highest_num = 0
	for i in range(len(arr)):
		for n in range(len(arr[i:])):
			current_highest_num = max(sum(arr[i:i+n+1]), current_highest_num)
	return current_highest_num
'''
#print(max_sequence([-2, -1, -3, -1, -5, -4]),6)
#print(max_sequence(lst1),155)


def next_bigger(n):
	#print(n)
	n = list(str(n))
	if len(n) == 1:
		return int(n[0])
	i=0

	catch1 = False
	while catch1 == False and i < len(n):
		#print(n[len(n)-i-1], n[len(n)-i-2])
		if n[len(n)-i-1] > n[len(n)-i-2]:
			n[len(n)-i-1], n[len(n)-i-2] = n[len(n)-i-2], n[len(n)-i-1]
			catch1 = True
		if catch1 == True and i == 0:
			return int(''.join(n))#, 'top'
		#print(i)
		i += 1
	i += 1
	catch2 = False
	while catch2 == False and i > 0:
		#print(n[len(n)-i-1] > n[len(n)-i-2])
		if n[len(n)-i-1] < n[len(n)-i-2]:
			n[len(n)-i-1], n[len(n)-i-2] = n[len(n)-i-2], n[len(n)-i-1]
			catch2 = True
		#print(i)
		i -= 1
	return int(''.join(n))#, 'bottom'


print(next_bigger(1234567890))

#print(next_bigger(122))