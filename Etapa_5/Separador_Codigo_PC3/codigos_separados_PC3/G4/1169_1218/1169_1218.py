from math import *
N = int(input("Digite um número: "))
cont = 1
k = 1
sf = (sqrt(cont) / (9 + k)) * -1
while(cont < N):
	if(cont % 2 == 0):
		k = k + 2
		cont = cont + 1
		sf = sf - (sqrt(cont)/ (9 + k))
	else:
		k = k + 2
		cont = cont + 1
		sf = sf + (sqrt(cont)/ (9 + k))

print(round(sf,6))