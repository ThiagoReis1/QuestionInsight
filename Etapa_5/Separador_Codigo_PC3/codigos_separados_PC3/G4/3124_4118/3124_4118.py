from numpy import*
v = array(eval(input("Vetor: ")))
i = 0
m = 1
while(i < len(v)):
	
	m = m*v[i]
	
	i = i +1
M = m**(1/len(v))
print(round(M,2))