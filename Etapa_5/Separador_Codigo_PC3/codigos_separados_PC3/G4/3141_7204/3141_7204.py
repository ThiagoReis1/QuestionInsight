from numpy import * 

v = array(eval(input("vetor: ")))

m = 0 

for i in range(size(v)):
	m = m + v[i]**(1/6)
	
M = (m/size(v))**6

print(round(M,2))