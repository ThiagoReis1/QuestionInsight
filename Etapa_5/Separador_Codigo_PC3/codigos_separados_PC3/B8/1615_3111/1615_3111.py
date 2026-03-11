from numpy import*

v = array(eval(input("Jogador um acertou quais ")))
cont = 0
Pontuacao = 0;
while(cont < size(v)):
	if(v[cont] == 1):
		Pontuacao += 40
	elif(v[cont] == 2):
		Pontuacao += 20
	elif(v[cont] == 3):
		Pontuacao += 10
	cont += 1
	
	
v2 = array(eval(input("Jogador dois acertou quais ")))
cont = 0
Pontuacao2 = 0;
while(cont < size(v)):
	if(v2[cont] == 1):
		Pontuacao2 += 40
	elif(v2[cont] == 2):
		Pontuacao2 += 20
	elif(v2[cont] == 3):
		Pontuacao2 += 10
	cont += 1
	
if(Pontuacao > Pontuacao2):
	print("JOGADOR UM")
elif(Pontuacao == Pontuacao2):
	print("EMPATE")
else:
	print("JOGADOR DOIS")
