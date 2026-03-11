x = float(input("digite o numero:"))
k = int(input("digite o numero:"))

contador = 0 
soma = 0
i = 1

while contador < k:
	soma = soma + (x **i)/i
	i = i + 2
	contador = contador + 1
print(round(soma,7))