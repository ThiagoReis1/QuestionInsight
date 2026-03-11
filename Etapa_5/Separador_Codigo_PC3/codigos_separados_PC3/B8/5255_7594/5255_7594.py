peso = float(input("Peso: "))
distancia = float(input("Distancia: "))
codigo = int(input("Codigo: "))

if codigo == 1:
	icms = 17.0
elif codigo == 2:
	icms = 17.5
elif codigo == 3:
	icms = 18.0
elif codigo == 4:
	icms = 20.0
	
total = (peso*25+distancia*0.1)*(1+icms/100)

print(round(total, 2))