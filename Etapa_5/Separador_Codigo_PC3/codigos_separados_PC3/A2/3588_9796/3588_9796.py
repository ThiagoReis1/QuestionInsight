from numpy import *
anel = array(eval(input("anel:")))
pontuacao = 10000.0
i=0
while i<size(anel):
	if anel[i] == 1:
		pontuacao = pontuacao * 2
	if anel[i] == 2:
		pontuacao = pontuacao
	if anel[i] == 3:
		pontuacao = pontuacao/2
	if anel[i] == 4:
		pontuacao = pontuacao/4
	i+=1
print(round(pontuacao,2))