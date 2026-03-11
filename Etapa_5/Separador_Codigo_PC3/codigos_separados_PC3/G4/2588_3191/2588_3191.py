from numpy import*
v = array(eval(input('')))
i = 0
for x in range(size(v)):
	if v[0]*1.20 < v[x] < v[0]*1.50:
		print(x)
		i += 1		
print(i)