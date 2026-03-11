e = float(input("horas extras? "))
f = float(input("horas que faltou? "))

h = e - (2 / 3) * f

if (h <= 600):
	g = 200.00
else:
	g = 300.00
	
print(e,"extras e",f,"de falta")
print("R$",round(g, 2))