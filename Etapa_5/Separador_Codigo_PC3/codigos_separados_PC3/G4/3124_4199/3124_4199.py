from numpy import*
from math import*
v = array(eval(input("vetor: ")))
n = 0

while(n < size(v)):
	m = (v[n]*v[n+1])**(1/n)
	
	
	n = n + 1 
print(round(m,2))