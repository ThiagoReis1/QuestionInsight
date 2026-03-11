from numpy import*
num = array(eval(input("insira os numeros: ")))

n = 0
for i in range(size(num)):
	n = n + 1

saida = zeros(n, dtype=int)
a = -1
for i in range(size(num)):
	saida[a] = saida[a] + num[i]
	a = a - 1
print(saida)
	