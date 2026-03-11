from numpy import *
dano = array(eval(input("")))
i = 0
acm = 0
while(i < size(dano)):
	novo = dano[i] * (i + 1)
	acm = acm + novo
	i = i + 1
	
print(acm)