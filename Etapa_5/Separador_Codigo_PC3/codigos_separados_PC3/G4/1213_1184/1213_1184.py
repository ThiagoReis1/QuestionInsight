from numpy import*
v = array(eval(input(" pesos:")))
rec = 217
c = 0
i = 0
print(rec)
while(c < size(v)):
	if (v[c] > rec):
		v[c] = i
		i = i+1
		print(i)
		
	c = c+1

