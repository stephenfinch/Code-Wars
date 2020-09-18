def num_of_open_lockers(n):
	doors = [False for x in range(1, n+2)]
	for i in range(1, n+1): # -1 = closed, 1 = open
		for j in range(1, n+1):
			if j % i:
				doors[j] = not doors[j]
				#print(j)
	return doors.count(True)

print(num_of_open_lockers(100))