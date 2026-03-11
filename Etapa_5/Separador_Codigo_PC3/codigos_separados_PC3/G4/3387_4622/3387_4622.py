uni = input("digite unidade: ")
valor = float(input("digite medida: "))


if(uni.upper() == "M"):
	kl = valor / 2.35215
	print(round(kl,2))
else:
	mg = 2.35215 * valor
	print(round(mg,2))
	
	
	