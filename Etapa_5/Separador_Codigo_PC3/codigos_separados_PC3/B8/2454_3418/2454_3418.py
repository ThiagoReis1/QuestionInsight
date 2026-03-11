from math import* 
#ENTRADA

altura = float(input("Altura: "))
sexo = input("Sexo: ").upper()

#CONDICIONAL

if((altura < 1.0) or (altura > 2.5)):
	print("altura invalida")
elif((sexo != "M") or (sexo != "F")):
	print("codigo invalido de sexo")
elif((altura >= 1.0) or (altura <= 2.5) and (sexo == "F")):
	peso_ideal = (round((62.1 * altura)- 44.7, 2))
	print(peso_ideal)
elif((altura >= 1.0) or (altura <= 2.5) and (sexo == "M")):
	peso_ideal = (round((62.1 * altura)- 58, 2))
	print(peso_ideal)
