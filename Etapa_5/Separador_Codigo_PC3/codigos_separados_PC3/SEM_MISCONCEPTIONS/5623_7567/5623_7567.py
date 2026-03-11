lanche = input("O que voce deseja? (B/S): ")
Quantl = int(input("Quantidade de fatias: "))
QuantC = int(input("Quantidade de cappuccinos: "))

B = 5.0
S = 4.0
C = 7.50

if(lanche.upper() == "B"):
	valor = (B * Quantl) + (C * QuantC)
	print(valor)
	
if(lanche.upper() == "S"):
	valor = (S * Quantl) + (C * QuantC)
	print(valor)