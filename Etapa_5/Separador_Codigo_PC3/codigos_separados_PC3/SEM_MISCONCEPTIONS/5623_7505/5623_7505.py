alimento = input()
qtd = float(input())
cap = float(input())

bolo = 5
salgado = 4
cappuccino = 7.5

if alimento == "B":
	eq = (bolo*qtd)+(cap*cappuccino)
	print(eq)
else:
	eq = (salgado*qtd)+(cap*cappuccino)
	print(eq)