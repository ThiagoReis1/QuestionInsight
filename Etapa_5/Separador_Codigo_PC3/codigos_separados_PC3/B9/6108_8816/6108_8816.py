ccomum = float(input("Quantidade de combustivel comum: "))

if ccomum >= 50:
	mistura = 4.7
	total = ccomum + mistura
	
elif ccomum > 35.0 and ccomum < 50.0:
	mistura = 3.3
	total = ccomum + mistura
	
elif ccomum > 17.5 and ccomum < 35.0:
	mistura = 2.3
	total = ccomum + mistura
	
else:
	mistura = 1.5
	total = ccomum + mistura
	
print(round(total,2))