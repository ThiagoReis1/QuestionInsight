from numpy import*

numeros = array(eval(input("Digite os numeros:")))


i = 0
v = 100
while i<size(numeros):
	if (numeros[i] == 1):
		v = v
	if (numeros[i] == 2):
		v = v * 2
	if (numeros[i] == 3):
		v = v/3
	if (numeros[i] == 4):
		v = v * 4
	if (numeros[i] == 5):
		v = v/5
	if (numeros[i] == 6):
		v = v * 6
	i = i + 1
pontuacao = v 
print(round(pontuacao,2))
	