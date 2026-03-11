volu = float(input("conta: "))

if (volu >= 0) and (volu <= 10):
	valor = volu * 3.00 + 15.00

elif(volu > 10) and (volu <= 15):
	valor = volu * 3.50 + 20.0

elif(volu > 15) and (volu < 20):
	valor = volu * 4.00 + 25.00
else:
	valor = volu * 4.50 + 30.0
	
print(round(valor, 2))