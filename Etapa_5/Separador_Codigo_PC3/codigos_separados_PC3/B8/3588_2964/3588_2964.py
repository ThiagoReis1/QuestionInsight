from numpy import *

aneis = array(eval(input()))

i = 0
pontuacao = 10000
while(i < size(aneis)):
	if(aneis[i] == 1):
		pontuacao = pontuacao * 2
	elif(aneis[i] == 3):
		pontuacao = pontuacao / 2
	elif(aneis[i] == 4):
		pontuacao = pontuacao / 4
	i += 1
	
print(round(pontuacao, 2))