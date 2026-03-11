from numpy import*

arco = array(eval(input('acertos do competidor:')))

i = 0
ponto = 10000

while i < size(arco):
	if arco[i] == 1:
		ponto *= 2
	elif arco[i] == 3:
		ponto /= 2
	elif arco [i] == 4:
		ponto /= 4
	i += 1
	
print(round(ponto,2))