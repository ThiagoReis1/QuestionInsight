from numpy import *

face = array(eval(input("Insira o valor da face do dado: ")))
				
i = 0
pontuacao_total = 200.
				 
while i < size(face):
	if face[i] == 1:
		pontuacao_total /= 2
	elif face[i] == 2:
		pontuacao_total *= 3
	elif face[i] == 3:
		pontuacao_total /= 2
	elif face[i] == 4:
		pontuacao_total *= 3
	elif face[i] == 5:
		pontuacao_total /= 2
	elif face[i] == 6:
		pontuacao_total *= 3
	i +=1
print(round(pontuacao_total, 2))
		
				 