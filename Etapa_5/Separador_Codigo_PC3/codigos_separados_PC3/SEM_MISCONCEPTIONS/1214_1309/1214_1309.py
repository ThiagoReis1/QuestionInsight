from numpy import *
v= array (eval(input("digite os pesos:")),dtype=int)

recorde=217

abaixo=0 # numero dos que estao abaixo
i=0     # variavel contadora
while (i<size(v)):
	if (v[i]<recorde): # se for menor acrescenta mais 1 aos que 
		abaixo = abaixo +1  # tao abaixo do recorde
	i=i+1
print(recorde)
print(abaixo)