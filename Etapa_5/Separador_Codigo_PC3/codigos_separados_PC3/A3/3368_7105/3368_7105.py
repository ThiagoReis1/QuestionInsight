tipo = input()
valor = float(input())

if(tipo == "c" or tipo == "C"):
	temperatura = valor + 273.15
if(tipo == "k" or tipo == "K"):
	temperatura = valor - 273.15
print(round(temperatura,2))
	
