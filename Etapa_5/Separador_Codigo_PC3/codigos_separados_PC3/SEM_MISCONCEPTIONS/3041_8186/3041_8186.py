from math import*

x = float(input("Diga o valor: "))

conta1 = -1/(x + 2)
conta2 = 1/(x-2)

if (2 < x ) and ( x <= 1000):
	print(round(conta2, 4))


elif (-1000 <= x) and ( x < (-2) ):
	print(round(conta1, 4))
	
else:
	print("entrada invalida")