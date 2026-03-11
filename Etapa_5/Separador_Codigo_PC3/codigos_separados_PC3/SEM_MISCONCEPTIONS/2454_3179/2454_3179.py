altura = float(input("Digite a altura: "))
sexo = input("(M / F): ")
peso1 = 72.7 * altura - 58
peso2 = 62.1 * altura - 44.7

if((sexo != "M") or (sexo != "F")):
	if(sexo == "M"):
		print(round(peso1, 2))
elif(sexo == "F"):
	print(round(peso2, 2))
else:
	print("codigo invalido de sexo")
   
  