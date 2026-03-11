from numpy import *
#entrada
v = float(input("Informe o numero  do vetor: "))

i = 0

v = ones(v, dtype = float)

while(i > v):
	if(v[i] > 8.95):
		i = i + 1
		print(v)
	else:
		print(v)
	
