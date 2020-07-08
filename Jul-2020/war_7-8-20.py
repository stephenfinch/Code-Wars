def reach_destination(distance, speed):
	num = distance/speed
	num = round(num * 2) / 2
	if num == 1.0:
		return 'The train will be there in 1 hour.'
	if str(num)[-1] == '0':
		return 'The train will be there in '+str(num)[:-2]+' hours.'
	return 'The train will be there in '+str(num)+' hours.'