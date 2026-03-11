from numpy import *

v = array(eval(input("Digite: ")))

i = 0
cont = 0

limite = (v[0] * 0.5) + v[0]

for i in range(size(v)):
	if(v[i] > limite):
		print(i)
		cont = cont + 1
print(cont)