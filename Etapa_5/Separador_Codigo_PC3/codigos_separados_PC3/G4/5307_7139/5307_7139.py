# Entrada

x = float(input("Numero real:"))
k = int(input("Numero inteiro:"))

# Repeticao

cont = 1
soma = 0

while (cont <= k):
	tg = (cont/x)
	soma = soma + tg
	cont = cont + 1
	
print(round(soma,10))
	
