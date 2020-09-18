import math

def num_of_open_lockers(n):
	open_doors = 0
	for i in range(1, n + 1):
		if (i**(.5) == int(i**(.5))): 
			open_doors += 1
	return open_doors


print(num_of_open_lockers(100))
