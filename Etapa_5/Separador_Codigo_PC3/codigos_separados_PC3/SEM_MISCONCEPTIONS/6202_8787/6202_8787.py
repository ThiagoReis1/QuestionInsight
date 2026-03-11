alt = float(input("digite altura: "))
txaluno = float(input("digite tx: "))
altbia = 1.69
txbia = 0.01
cont = 0

while altbia <= alt:
	if txbia > txaluno: 
	   alt = alt + txaluno
	   cont = cont + 1
	print(alt)
else: alt > altbia
print(alt)
	
	