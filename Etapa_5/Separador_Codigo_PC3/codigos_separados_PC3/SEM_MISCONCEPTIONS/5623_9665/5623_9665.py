Cm = input("bolo ou salgado? ").upper()
Quantc = float(input("digite a quantidade: "))
quantCap = float(input("digite a quantidade de cappuccinos: "))

if Cm == "B":
	vt = Quantc * 5.00 + quantCap * 7.50
	print(round(vt,2))
else:
	vt = Quantc * 4.00 + quantCap * 7.50
	print(round(vt,2))