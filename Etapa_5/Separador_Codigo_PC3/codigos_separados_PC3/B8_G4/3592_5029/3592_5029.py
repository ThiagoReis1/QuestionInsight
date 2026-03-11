from numpy import *
v = array(eval(input("")))

p = 100
a = 0
i = 0

while (i < size(v)) :
	if (v[i] == 1) :
		p = p + a
		i = i + 1
	elif (v[i] == 2) :
		p = p*2 + a
		i = i + 1
	elif (v[i] == 3) :
		p = p/3 + a
		i = i + 1
	elif (v[i] == 4) :
		p = p*4 + a
		i = i + 1
	elif (v[i] == 5) :
		p = p/5 + a
		i = i + 1
	elif (v[i] == 6) :
		p = p*6 + a
		i = i + 1
print(round(p,2))
