from numpy import * 

v = array(eval(input("Coordenada so vetor: ")))
m = 0
for i in range(size(v)):
	m = m + (exp(v[i])) / exp(size(v))
print(round(log(m),2))