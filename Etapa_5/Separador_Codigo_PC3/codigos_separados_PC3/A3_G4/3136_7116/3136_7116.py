from numpy import*

n = array(eval(input(": ")))
m = 0
v = 0

for i in range (size(n)):
	m = m + log (n[i] + 1 )
	
g = exp (m/size(n)) -1

print(round(g, 2))