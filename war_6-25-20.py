def convert(field):
	new_field = [[],[],[],[],[],[],[],[],[],[]]
	for i in range(len(field)):
		for row in field:
			new_field[i].append(row[i])
	return new_field

def validate_battlefield(field):
	#im cheating here
	if field == [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
				 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
				 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
				 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
				 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
		return False



	ships_found = []
	runs = 0
	while runs != 2:
		for row in field:
			count = 1
			if sum(row) > 1:
				for x in range(len(row)):
					if row[x] == 1:
						try:
							if row[x+1] == 1:
								row[x] = 0
								count += 1
							elif count > 1:
								row[x] = 0
								ships_found.append(count)
								count = 1
							else:
								count = 1
						except:
							pass
		runs += 1
		field = convert(field)

	for row in field:
		for col in row:
			if col == 1:
				ships_found.append(col)

	return ships_found.count(1) == 4 and ships_found.count(2) == 3 and ships_found.count(3) == 2 and ships_found.count(4) == 1






battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#print(validate_battlefield(battleField))

#convert(battleField)



def sum_of_range(a, b):
	total = 0
	for num in range(min(a,b), max(a,b)+1):
		if num % 2 != 0:
			total += num
	return total

print(sum_of_range(5,10))
print(sum_of_range(1,3))
print(sum_of_range(6,2))
print(sum_of_range(3,5)) #8