'''
def num_of_open_lockers(n):
	doors = []
	for i in range(1, n + 1):
		count = 0
		for j in range(1, i + 1):
			if i % j == 0:
				count += 1
		doors.append(count % 2 == 0)
	return doors.count(False)
'''
import math

def num_of_open_lockers(n):
	open_doors = 0
	for i in range(1, n + 1):
		if math.sqrt(i) == math.floor(math.sqrt(i)):
			open_doors += 1
	return open_doors


print(num_of_open_lockers(100))
