
from numpy import*

ct = array(eval(input("Custo: ")))
soma = sum(ct)
i = 0 
cont = 0

while(i < size(ct)):
	if ct[i] > 160:
		cont = cont + 25
	i = i + 1

cl = soma - cont
print(round(cl,2))