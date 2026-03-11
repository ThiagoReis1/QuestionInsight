btu = "B"
watt = "W"
uni = input("")
med=float(input("medida: "))
if uni == watt:
	btu = 3.41214 * med
	print(round(btu,2))
else:
	watt = med/(3.41214)
	print(round(watt,2))