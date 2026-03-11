altura = float(input("insira a altura"))
sexo = (input("insira o sexo"))

if(sexo=="M") and ((altura>=1.0) and (altura<=2.5)):
	pesoM = (72.7*altura)-58
	print(round(pesoM,2))
elif(sexo=="F") and ((altura>=1.0) and (altura<=2.5)):
	pesoF = (62.1*altura)-44.7
	print(round(pesoF,2))
elif(altura>=2.5) or (altura<=1.0):
	print("altura invalida")
elif(sexo!="M") or (sexo!="F"):
	print("codigo invalido de sexo")


