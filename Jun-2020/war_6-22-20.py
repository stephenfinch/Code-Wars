def solution(args):
	output = []
	current = args[0]
	start = args[0]
	bits = {args[0]:args[0]}
	for item in args:
		#print(bits, item)
		if item-current == 1:
			bits.update({start:item})
		else:
			bits.update({item:item})
			start = item
		current = item

	for key, value in bits.items():
		if value-key == 1:
			output.append(str(key))
			output.append(str(value))
		if key == value:
			output.append(str(key))
		if value-key > 1:
			output.append(str(key)+'-'+str(value))

	return ','.join(output)


#print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')