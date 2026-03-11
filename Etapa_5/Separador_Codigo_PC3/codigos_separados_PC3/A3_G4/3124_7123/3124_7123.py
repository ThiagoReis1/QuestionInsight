from numpy import*

v = array(eval(input(": ")))
a = 1
b = 0

for i in range (size(v)):
	a = a * (v[i])
	
m = a**(1/(size(v)))	
	
print(round(m, 2))