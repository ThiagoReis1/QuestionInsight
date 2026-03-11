from numpy import *
p = array(eval(input("andares em que parou: ")))
i = 0 #indice
q = -1
c = 0
while(i<size(p)):
	m = abs(p[q]-p[q-1])
	c = c + m 
	i = i + 1
	
print(c)	