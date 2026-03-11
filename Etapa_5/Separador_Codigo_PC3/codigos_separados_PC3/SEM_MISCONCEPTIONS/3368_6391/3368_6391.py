escala = input("Escolha a escala desejada, C para Celsius ou K para Kelvin: ")
Escala = escala.upper()

temperatura = float(input("Determine uma temperatura para ser convertida: "))

if (Escala == "C") :
	conversao = temperatura + 273.15
else :
	conversao = temperatura - 273.15
	
print(round(conversao, 2))
