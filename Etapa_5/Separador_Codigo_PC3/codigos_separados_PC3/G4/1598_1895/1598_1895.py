from numpy import *

custos = array(eval(input("digite os valores")))
p = 0
cont = 0
i = size(custos)
while( cont < i):
	p = p + custos[cont]
	if( custos[cont] > 80.0):
		p = p - 5.0
	cont = cont + 1
print(round(p,2))