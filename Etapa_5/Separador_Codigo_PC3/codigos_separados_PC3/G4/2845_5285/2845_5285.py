from numpy import *

v = array(eval(input("Digite o codigo: ")))

n = size(v)

for i in range(n):
	if v[i] >= 9  :
		v[i] = 0
	else :v[i] = v[i] + 1	
		
print(v)