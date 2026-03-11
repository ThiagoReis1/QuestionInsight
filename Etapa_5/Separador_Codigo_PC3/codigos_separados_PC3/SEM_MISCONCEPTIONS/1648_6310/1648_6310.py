from numpy import array,size,zeros
entrada = array(eval(input()))
qntReprovados = 0
for i in range(0, size(entrada)):
	if(entrada[i] < 70):
		qntReprovados += 1
posicoes = zeros(qntReprovados, dtype=int)
indice = 0
for i in range(0, size(entrada)):
	if(entrada[i] < 70):
		posicoes[indice] = i
		indice += 1
print(qntReprovados)
print(posicoes)