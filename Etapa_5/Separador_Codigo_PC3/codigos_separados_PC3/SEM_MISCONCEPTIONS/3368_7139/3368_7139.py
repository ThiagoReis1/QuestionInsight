#Entrada

escala = input("Escala da temperatura:")
temperatura = float(input("Digite a temperatura:"))

if escala.upper() == "C":
	conversao = temperatura + 273.15
else:
	conversao = temperatura - 273.15
	
# Saida 

print(round(conversao,2))