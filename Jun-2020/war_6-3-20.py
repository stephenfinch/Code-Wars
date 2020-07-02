def first_non_repeating_letter(s):
	s_low = s.lower()
	for char in list(s):
		if list(s_low).count(char.lower()) == 1:
			return char
	return ''


#print(first_non_repeating_letter('moonmen'), 'e')
#print(first_non_repeating_letter('~><#~><'), '#')
#print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')
import math

def removNb(n):
	output = {}
	n = list(range(1,n+1))
	total = sum(n)
	#n = n[math.floor(total/len(n)):]
	a = math.floor(total/len(n))
	while a < len(n):
		try: #if b is in n
			if (total-n[a])/(n[a]+1) <= total:
				output.update({n[a]:(n[a],int((total-n[a])/(n[a]+1)))})
				a += 1
		except: #if b is not in n
			n.remove(n[a])
			# do something with a here?
		#print(n, a)

	return list(output.values())

print(removNb(100000))


def t(n):
	n = list(range(1,n+1))
	return n, sum(n)
#print(t(26))



def r(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1,n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol, total


#print(r(26))