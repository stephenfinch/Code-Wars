def num_of_open_lockers(n):
	doors = []
	for i in range(1, n + 1):
		factors=[]
		for j in range(1, i + 1):
			if i % j == 0:
				factors.append(j)
		doors.append(len(factors) % 2 == 0)
	return doors.count(False)


print(num_of_open_lockers(100))
