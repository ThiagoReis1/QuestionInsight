# faça seu código aqui!
from numpy import *

n = input("").upper()
i = 0
cont = 0
while(i < len(n)):
	if n[i] == 'C':
		cont = cont + 1
	i = i + 1
print(cont)
		
		