def over_the_road(address, n):
	#if address % 2 == 0:

	houses = {}
	left = 1
	right = n*2
	for i in range(1, n+1):
		houses.update({i:[left, right]})
		left += 2
		right -= 2
	return houses



'''

 1|   |12
 3|   |10
 5|   |8
 7|   |6
 9|   |4
11|   |2

'''