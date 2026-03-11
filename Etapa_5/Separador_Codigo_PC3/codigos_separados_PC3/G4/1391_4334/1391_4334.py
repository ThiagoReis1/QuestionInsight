# X eh o consumo do usuario em kWh
X = int(input("digite um numero: "))
# Y eh o valor da conta em reais
if (X<=150):
	Y=(0.60*X)+5.00
	print(round(Y,2))
else:
	Y=(0.75*X)+16.00
	print(round(Y,2))