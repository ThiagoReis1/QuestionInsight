# Entrada de variaveis

tempovoo = float(input("Quanto tempo ocorreu o voo: "))

# Calculando as variaveis

temp200 = 5000 + (100 * tempovoo)
tempomaior = 8000 + (200 * 100) + (90 * (tempovoo - 200))

# Saida de variaveis

if tempovoo <= 200:
	
	tempototal = temp200

else: 
	tempototal = tempomaior
	
print(round(tempototal, 2))