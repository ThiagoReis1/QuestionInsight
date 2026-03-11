from numpy import*

v = array(eval(input()))
i = 0
g = 0 
c = 0

for i in range(size(v)):
	if v[i] == 99:
		v[i] = 0 
		g = g*2
	g = g + v[i]
print(g)