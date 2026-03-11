from numpy import* 

c = array(eval(input(": ")))
i = 0 

while i < size(c) :
	if c[i] > 80:
		c[i] = c[i] - (15/100)*c[i]
	else:
		c[i]= c[i]
	i = i + 1

t = sum(c)
	
print(round(t,2))
	