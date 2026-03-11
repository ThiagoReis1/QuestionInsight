from numpy import*

notas = array(eval(input('Digite as duas notas:')))

i = 0
media = 0


notas[0] = notas[0] * 4
notas[1] = notas[1] * 3

total = notas[0] + notas[1]	
	

media = total / 7

print(round(media, 2))
	