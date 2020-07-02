def iq_test(n):
	n = n.split(' ')
	even = []
	odd = []
	for i in range(len(n)):
		if int(n[i]) % 2 == 0: #these are even
			even.append(i)
		else:
			odd.append(i)
	if len(even) == 1:
		return even[0]+1
	else:
		return odd[0]+1

#print(iq_test('4 5 4 6'))


def snail(map):
	if map[0] == []:
		return []
	row = 0
	col = 0
	output = []
	chipR = 0 #chip away at the box
	chipD = 0
	chipL = 0 
	chipU = 0
	val = 'r' 
	while len(map)**2 > len(output):
		
		if val == 'r':
			if col == len(map)-chipR:
				val = 'd'
				chipR += 1
				row += 1
				col -= 1
				print('going right and hit the edge')
			else:
				output.append(map[row][col])
				print(output, col, row, val, chipR, chipD, chipL, chipU)
				col += 1
		if val == 'd':
			if row == len(map)-chipD:
				val = 'l'
				chipD += 1
				col -= 1
				row -= 1
				print('going down and hit the edge')
			else:
				output.append(map[row][col])
				print(output, col, row, val, chipR, chipD, chipL, chipU)
				row += 1
		if val == 'l':
			if col == -1+chipL:
				val = 'u'
				chipL += 1
				row -= 1
				col += 1
				print('going left and hit the edge')
			else:
				output.append(map[row][col])
				print(output, col, row, val, chipR, chipD, chipL, chipU)
				col -= 1
		if val == 'u':
			if row == 0+chipU:
				val = 'r'
				chipU += 1
				col += 1
				row += 1
				print('going up and hit the edge')
			else:
				output.append(map[row][col])
				print(output, col, row, val, chipR, chipD, chipL, chipU)
				row -= 1

	return output

#print(snail([[5,4],
#			 [3,2]]))

#print(snail([[5,4,6],
#			 [2,2,3],
#			 [9,7,5]]))

#print(snail([[1,2,3,4],
#			 [12,13,14,5],
#			 [11,16,15,6],
#			 [10,9,8,7]]))

print(snail([[1,2,3,4,5],
			 [16,17,18,19,6],
			 [15,24,25,20,7],
			 [14,23,22,21,8],
			 [13,12,11,10,9]]))