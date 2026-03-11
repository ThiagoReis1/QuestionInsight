qtde = int(input("insira a qtde desconhecida: "))

cont = 0

while (qtde != -1):
	if (qtde >= 76) and (qtde <= 100):
		cont += 1
	qtde = int(input("insira a qtde desconhecida: "))
print(cont)
