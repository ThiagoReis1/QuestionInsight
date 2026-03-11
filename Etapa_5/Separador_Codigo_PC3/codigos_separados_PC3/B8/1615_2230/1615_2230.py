from numpy import *

j1 = array(eval(input("Digite um vetor: ")))
j2 = array(eval(input("Digite um vetor: ")))

i = 0
cont1 = 0
cont2 = 0
while(i<size(j1) and i<size(j2)):
	if(j1[i]== 1 or j1[i]== 2 or j1[i] == 3 or j1 == 4):
		cont1 = cont1 + 1
	elif(j2 == 1 or j2[i] == 2 or j2[i] == 3 or j2[i] == 4):
		cont2 = cont2 + 1
	i = i + 1
if(j1>j2):
	print("JOGADOR UM")
elif(j2>j1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")