from numpy import*
vet1 = (array(eval(input("primeiro jogador:"))))
vet2 = (array(eval(input("segundo jogador:"))))
i = 0

while(size(vet1) > i):
	if(vet1[i] == 1):
		vet1[i] = 40
	elif(vet1[i] == 2):
		vet1[i] = 20
	elif(vet1[i] == 3):
		vet1[i] = 10
	elif(vet1[i] == 4):
		vet1[i] = 0
	if(vet2[i] == 1):
		vet2[i] = 40
	elif(vet2[i] == 2):
		vet2[i] = 20
	elif(vet2[i] == 3):
		vet2[i] = 10
	elif(vet2[i] == 4):
		vet2[i] = 0
	
	i = i + 1
if(sum(vet1) > sum(vet2)):
	print("JOGADOR UM")
elif(sum(vet2) > sum(vet1)):
	print("JOGADOR DOIS")
elif(sum(vet1) == sum(vet2)):
	print("EMPATE")

	