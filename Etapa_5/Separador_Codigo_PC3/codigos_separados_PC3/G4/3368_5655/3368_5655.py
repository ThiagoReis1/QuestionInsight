esc = input("Defina a escala: ")
temp = float(input("Temperatura: "))

if(esc.upper() == "C"):
	grau = temp + 273.15
else:
	grau = temp - 273.15

print(grau)