from numpy import *

atk = array(eval(input("Digite: ")))
i = 0
j = 2
dano = 0
while(i<size(atk)):
	dano = +(atk[i]*j+1)
	j = j+1
	i = i+1
print(dano)