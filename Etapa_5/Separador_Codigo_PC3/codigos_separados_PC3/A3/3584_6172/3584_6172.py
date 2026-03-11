from numpy import*

c = array(eval(input()))
i = 0
custo = 0 
while i < size(c):
	if c[i] > 200:
		c[i] = c[i]-c[i]*0.15
	i = i + 1

print(round(sum(c),2))
