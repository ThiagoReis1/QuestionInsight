altura= float(input("Qual a altura? "))
sexo= input("Qual o sexo M ou F? ")

if((sexo == "M") or (sexo == "F")) and ((altura >= 1) and (altura <= 2.5)):
	if(sexo == "M"):
		peso= (72.7 * altura) - 58
		print(round(peso, 2))
	elif(sexo == "F"):
		peso= (62.1 * altura) - 44.7
		print(round(peso, 2))
else:
	if(altura < 1) or (altura > 2.5):
		print("altura invalida")
	elif(sexo != "M") or (sexo != "F"):
		print("codigo invalido de sexo")