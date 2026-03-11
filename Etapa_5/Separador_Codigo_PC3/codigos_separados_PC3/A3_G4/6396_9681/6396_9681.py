from numpy import*
r = array(eval(input("")))
i = 0

for x in range(0 ,size(r), 1):
	if r[x] == 0:
		r[x] = 0
	else :
		r[x] *= 2
					
print(r)					