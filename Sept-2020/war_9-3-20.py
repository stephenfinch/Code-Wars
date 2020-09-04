def number(lines):
	return [str(x)+': '+lines[x-1] for x in range(1, len(lines) + 1)]


import random

a = ['the new world order','barack obama','hillary clinton', 'black lives matter','interdimensional vampires','the elites','repilians','china','mexicans','antifa','the liberal media','satanists','the gays','muslims','the jews','elon musk','the CIA','ISIS']
b = ['are spying on','are collecting data on','are profiting from','are putting chemicals into','are lying about','are mind controlling','are crossbreeding with','are sacrifficing','are brainwashing','are fabricating evidence against', 'are censoring','are microshipping','are tracking','are plotting to assassinate','are experimenting on']
c = ['christain children','white men','donald trump','conservatives','gun owners','the frogs','teenage boys','straight married couples','unborn babeis','members of the right wing media']
d = ['to establish a new world order','to turn them gay','to cover up 9/11','to destroy the nuclear family','to achieve eternal life','to spread a satanist agenda','to start world war III','to suppress the population','to control the media narrative','to take away our guns','to overthrow the US government']

def political_stance():
	a_pick = a[random.randint(0,len(a)-1)]
	b_pick = b[random.randint(0,len(b)-1)]
	c_pick = c[random.randint(0,len(c)-1)]
	d_pick = d[random.randint(0,len(d)-1)]
	stance = [a_pick,b_pick,c_pick,d_pick]
	print(' '.join(stance)+'!!')

political_stance()