from numpy import*

v = array(eval(input(" ")))
m = 0

for i in range(size(v)):
	m = m + log(v[i] + 1)
	
g = exp(m/size(v)) - 1

print(round(g, 2))