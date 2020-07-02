import math

def cakes(r, s):
	need = list(r.keys())
	bake = []
	for i in range(len(r)):
		try:
			bake.append(math.floor(s.get(need[i])/r.get(need[i])))
		except:
			return 0
	return min(bake)

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))