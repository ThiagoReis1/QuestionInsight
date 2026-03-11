from numpy import*

v = array(eval(input(" ")))

i = 0
pontuacao = 0

while(i<4):
	if(v[i]  == 1):
		ponto = 80
	elif(v[i] == 2):
		ponto = 40
	elif(v[i] == 3):
		ponto = 20
	elif(v[i]>=4):
		ponto = 0
		i = 4
	if(i<4):
		pontuacao = pontuacao + ponto
	i = i + 1
print(int(pontuacao))