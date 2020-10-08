def pairs(a):
	b = [abs(a[i] - a[i+1]) for i in range(0, len(a)-1, 2)]
	return b.count(True)
	


#print(pairs([1,2,5,8,-4,-3,7,6,5]),3)
#print(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]),2)



def square_digits(num):
	return int(''.join(str(int(x)**2) for x in str(num)))

print(square_digits(9119))