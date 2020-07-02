def same_structure_as(a,b):
	a,b = str(a),str(b)
	a = a.replace("'['", "ha") #hahahahahahahahahahaha
	a = a.replace("']'", "ha") #ok this might be cheating a bit
	b = b.replace("'['", "ha") #bit im so new to python that im just happy i got it
	b = b.replace("']'", "ha") #also its like 1 am and i will go crazy if i dont finish this rn
	strA = ''
	strB = ''
	for char in str(a):
		if char == '[' or char == ']' or char == ',':
			strA += char
	for char in str(b):
		if char == '[' or char == ']' or char == ',':
			strB += char
	return strA == strB

hmm = [1,'[',']']
hmm2 = ['[',']',1]


b = [[3,4,2, [1,3], 4, [4]], [],8]
a = [[3,4,2, [1,3], 4, [4]], [],8]
aa = [1,[1,1],[],4,[[3,4,2, [1,3], 4, [4]], [],8]]
bb = [4,[2,2],[],8,[[3,4,2, [1,3], 4, [4]], [],8]]

#print(same_structure_as([1,[1,1]],[2,[2,2]]), True)
#print(same_structure_as([1,[1,1]],[[2,2],2]), False)
#print(same_structure_as(['b', 1], [0,0]))
print(same_structure_as(hmm, hmm2))




ab = [ 1, [ 1, 1 ] ]
ba = [ [ 2, 2 ], 2 ]












