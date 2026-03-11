from numpy import * 

v = array(eval((input("numeros: "))))

m = 0

for i in range(size(v)):
	m = m + log(v[i] + 1)
	
M = exp(m/size(v)) -1
print(round(M,2))