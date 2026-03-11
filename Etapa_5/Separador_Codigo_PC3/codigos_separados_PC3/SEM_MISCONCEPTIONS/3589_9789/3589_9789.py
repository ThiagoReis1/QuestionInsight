from numpy import *
arco = array(eval(input("")))

i = 0 
pontos = 0 

while i < size(arco):
	if arco[i] == 1:
	 	pontos += 80
	if arco[i] == 2:
		pontos += 40
	if arco[i] == 3:
		pontos += 20
	if arco[i] == 4:
		pontos += 10
	i += 1 

print(pontos)