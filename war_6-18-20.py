def smallest(s):
	n = []
	for num in str(s):
		n.append(int(num))
	new_list = []
	while not new_list:
		for i in range(len(n)):
			if n[i] == min(n):
				new_list = [n[i]] + n[:i]+n[i+1:]
	return int(''.join(map(str,new_list)))

def smallest(s):
	print(s)
	n, new_list, i = [], [], 0
	for num in str(s):
		n.append(int(num))
	while len(new_list) < len(n):
		index = n.index(min(n))
		if index == 0:
			new_list.append(n[0])
			n = n[1:]
		else:
			x = len(new_list)
			#print('--------', n)
			new_list += [min(n)] + n[:index] + n[index+1:]
		i += 1

	if index+x == 1 and x == 0:
		x, index = 1, -1
	return [int(''.join(map(str,new_list))), index+x, x]


print(61879470434<60187947434)
#print(smallest(125554))#, [126235, 2, 0])
#print(smallest(261235), [126235, 2, 0])