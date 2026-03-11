from numpy import*
matriz = array(eval(input("codigo secreto: ")))
saida = zeros(matriz, dtype=int)
for i in range(size(matriz)):
	matriz[i] = matriz[i] * 2
print(matriz)