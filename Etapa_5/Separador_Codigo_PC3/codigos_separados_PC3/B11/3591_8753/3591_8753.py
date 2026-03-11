from numpy import*
jogadas = array(eval(input("jogadas: ")))
i = 0
pontos = 0
while i < size(jogadas):
	if jogadas[i] == 1:
		pontos = pontos + 10
	if jogadas[i] == 2:
		pontos = pontos + 5
	if jogadas[i] == 3:
		pontos += 10
	if jogadas[i] == 4:
		pontos += 5
	if jogadas[i] == 5:
		pontos += 10
	if jogadas[i] == 6:
		pontos += 5
	i += 1
print(pontos)