from numpy import*

v = array(eval(input("Acertou qual ")),dtype=int)
cont = 0
Pontuacao = 0;
while(v[cont] < 4):
	if(v[cont] == 1):
		Pontuacao += 80
	elif(v[cont] == 2):
		Pontuacao += 40
	elif(v[cont] == 3):
		Pontuacao += 20
	cont += 1
	
print(Pontuacao)