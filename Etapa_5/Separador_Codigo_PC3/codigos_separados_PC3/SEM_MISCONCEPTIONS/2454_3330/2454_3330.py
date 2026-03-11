altura = float(input("digite a altura:"))

sexo = input("digite sexo M ou F:")

if (altura < 1.0) or  (altura > 2.5):
	print("altura invalida")
elif (sexo !="M")	and (sexo !="F"):
	print("codigo invalido de sexo")
elif (sexo =="M"):
	homem = (72.7 * altura) - 58
	print(round(homem, 2))
else:
	mulher = (62.1 *altura) - 44.7
	print(round(mulher, 2))