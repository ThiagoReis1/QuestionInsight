from numpy import*
v1 = array (eval (input ("primeiro jogador: ")))
v2 = array (eval (input ("segundo jogador: ")))

i = 0
j = 0
soma = 0
soma2 = 0

while (i < size(v1)):
	if (v1[i] == 1):
		soma = soma + 40
	elif (v1[i] == 2):
		soma = soma + 20
	elif (v1[i] == 3):
		soma = soma + 10
	elif (v1[i] >= 4):
		soma = soma + 0
	i = i + 1
	
while (j < size(v2)):
	if (v2[j] == 1):
		soma2 = soma2 + 40
	elif (v2[j] == 2):
		soma2 = soma2 + 20
	elif (v2[j] == 3):
		soma2 = soma2 + 10
	elif (v2[j] >= 4):
		soma2 = soma2 + 0
	j = j + 1
	
if (soma > soma2):
	print ("JOGADOR UM")
elif (soma2 > soma):
	print ("JOGADOR DOIS")
else:
	print ("EMPATE")