from numpy import*
m = array(eval(input()))
lin = shape(m)[0]
col = shape(m)[1]
indice = 0
#no teu codigo vai ser em vez de menor maior = 0
menor = 999999999999999999999999
for i in range(lin):
	for j in range(col):
		#aqui tu muda so o sinal
		if (m[i][j] < menor):
			indice = 1
			menor = m[i][j]
		else:
			j = j + 1
print(menor)