Ds = int(input("digite a distancia: "))

Pi = 50.00

if Ds < 10:
	Pf = Pi + 5.50
	print(round(Pf,2))
elif Ds == 10:
	Pf = Pi + 7.75
	print(round(Pf,2))
else:
	Pf = Pi + 10.00
	print(round(Pf,2))
