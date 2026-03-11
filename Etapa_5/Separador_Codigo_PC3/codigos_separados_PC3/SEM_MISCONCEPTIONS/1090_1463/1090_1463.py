#Ingrid do Nascimento Mendes
#30/06/2016

compra1 = float(input())
compra2 = float(input())
compra3 = float(input())
compra4 = float(input())
limite = float(input())

total = compra1 + compra2 + compra3 + compra4

print(round(total,2))

if (limite>=total):
	print("Sim")
else:
	print("Nao")