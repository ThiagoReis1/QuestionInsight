from numpy import *

n = array(eval(input("Entre com um vetor: ")))
i = 0 
m = 0

while (i < size(n)):
	m = m + (n[i]**0.5)
	i = i + 1

total = (m/size(n))**2
print(round(total, 2))


