from numpy import*
custo = array(eval(input("Digite o custo do produto: " )))
i = 0
n = size(custo)
custo_compra = zeros(n, dtype = float)

while (i < size(custo)):
	if (custo[i] >= 80):
		custo_compra[i] = custo[i] - 5
	else:
		custo_compra[i] = custo[i]
	i = i + 1

print(round(sum(custo_compra),2))
	