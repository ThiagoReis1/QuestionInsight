# faça seu código aqui!
entradas = input()
qtde = int(input())
if entradas.upper() == "B":
	valor = 25.90 * qtde
	valor = valor - valor * 10/100
else:
	valor = 25.90 * qtde
print(round(valor, 2))
