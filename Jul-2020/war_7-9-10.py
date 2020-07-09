def find_num(n):
	numbers_used, current_digets, number = [0], [0], 0
	for i in range(n):
		test, keep_looking = 0, True
		while keep_looking:
			if test not in numbers_used:
				diget_test = True
				for diget in str(test):
					if int(diget) in set(current_digets):
						diget_test = False
				if diget_test:
					number, keep_looking = test, False
					numbers_used.append(number)
					current_digets = [int(x) for x in str(number)]
			test += 1
	return number



#is it being used in the seq already?
#does it share any digets with the last number?


#when a new number is found:
	#update the number
	#update the numbers_used
	#update the current_digets