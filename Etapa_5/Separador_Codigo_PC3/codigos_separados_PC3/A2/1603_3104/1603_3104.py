from numpy import*

num=array(eval(input()))
i=0
pontuacao=0

while(num[i] != 4 and num[i] <= 4 and i<size(num)):
	if(num[i] == 1):
		pontuacao = pontuacao + 80 
	if(num[i] == 2):
		pontuacao = pontuacao + 40
	if(num[i] == 3):
		pontuacao = pontuacao + 20
	else: 
		pontuacao = pontuacao
	i = i+1
	
print(pontuacao)