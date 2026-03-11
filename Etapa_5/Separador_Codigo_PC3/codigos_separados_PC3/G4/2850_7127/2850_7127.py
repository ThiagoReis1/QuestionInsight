from numpy import *

v = array(eval(input("Digite o vetor: ")))

n = 0

for i in range(size(v)):
	n = n + v[i]
	if(n >= 55):
		n = 0

print(n)
		
