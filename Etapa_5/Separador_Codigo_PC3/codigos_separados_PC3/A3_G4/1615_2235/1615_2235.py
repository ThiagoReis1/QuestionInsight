from numpy import *

jo1 = array(eval(input("Digite o valor de jogadas 1: ")))
jo2 = array(eval(input("Digite o valor de jogadas 2: ")))
i = 0
while( i < size(jo1)):
	if(jo1[i] == 1):
		j1 = j1 + 40
	elif(jo1[i] == 2):
		j1 = j1 + 20
	elif(jo1[i] == 3):
		j1 = j1 + 10
	else:
		j1 = j1 + 0
	i = i + 1
	
i = 0
while(i < size(jo2)):
	if(jo2[i] == 1):
		j2 = j2 + 40
	elif(jo2[i] == 2):
		j2 = j2 + 20
	elif(jo2[i] == 3):
		j2 = j2 + 10
	else:
		j2 = j2 + 0
	i = i + 1
	
if(j1 > j2):
	mensagem = "Jogador 1"
elif(j1 < j2):
	mensagem = "Jogador 2"
else:
	mensagem = "Empate"
	
print(j1,j2)