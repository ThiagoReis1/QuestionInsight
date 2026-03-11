from numpy import*

frutas = array(eval(input("Digite as frutas: ")))
gramas = array(eval(input("Digite as gramas ingeridas: ")))

i = 0
kcal = 0

while (i != size(frutas)):
	if(frutas[i] == "BANANA"):
		kcal = (gramas[i] * 0.97) + kcal
	elif (frutas[i] == "BIFE"):
		kcal = (gramas[i] * 2.95) + kcal
	elif (frutas[i] == "FEIJOADA"):
		kcal = (gramas[i] * 1.27) + kcal
	elif (frutas[i] == "OMELETE"):
		kcal = (gramas[i] * 1.04) + kcal
	elif (frutas[i] == "TOMATE"):
		kcal = (gramas[i] * 0.2) + kcal
	i = i+1
	
print(round(kcal, 2))