altmac = 1.86
txmac = 0.01
altcol = float(input("altura do coelho: "))
txcol = float(input("taxa de crescimento: "))
cont = 0

while altcol < altmac:
	altcol = altcol + txcol
	altmac = altmac + txmac
	cont = cont + 1
print(cont)