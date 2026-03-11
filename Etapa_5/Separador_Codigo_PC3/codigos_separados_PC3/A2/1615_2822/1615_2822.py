from numpy import*

num_1 = array(eval(input("Jogador 1: ")))
num_2 = array(eval(input("Jogador 2: ")))

i = 0
soma1 = 0
soma2 = 0
while(i<size(num_1)):
	if(num_1[i] == 1):
		soma1 = soma1 + 40
	elif(num_1[i] == 2):
		soma1 = soma1 + 20
	elif(num_1[i] == 3):
		soma1 = soma1 + 10
	else:
		soma1 = soma1
	if(num_2[i] == 1):
		soma2 = soma2 + 40
	elif(num_2[i] == 2):
		soma2 = soma2 + 20
	elif(num_2[i] == 3):
		soma2 = soma2 + 10
	else:
		soma2 = soma2
	i = i + 1
		

if(soma2 < soma1):
	print("JOGADOR UM")
elif(soma1 == soma2):
	print("EMPATE")
else:
	print("JOGADOR DOIS")