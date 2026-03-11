from numpy import * 

aneis = array(eval(input('quais foram os acertos?')))

i = 0
pontos = 100

while i < size(aneis):
	if aneis[i] == 1:
		pontos *=5
	elif aneis[i] == 2:
		pontos *=3
	elif aneis[i] == 3:
		pontos = pontos
	elif aneis[i] == 4:
		pontos = pontos/2
	i += 1
	
print(round(pontos,2))