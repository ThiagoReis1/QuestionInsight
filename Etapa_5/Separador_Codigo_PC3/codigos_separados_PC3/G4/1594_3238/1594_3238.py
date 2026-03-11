from numpy import *
ataque = array(eval(input(":")))
i = 0
j = 1
dano = 0
while(i<size(ataque)):
	dano=dano+(ataque[i]*j)
	j=j+1
	i=i+1
print(dano)