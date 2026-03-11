dia = int(input("Digite a quantidade de dias: "))
if(dia < 15):
	valor = (dia * 175) + 20
	print("total=", valor)
elif(dia == 15):
	valor = (dia * 175) + 16
	print("total=", valor)
else:
	valor = (dia * 175) + 10
	print("total=", valor)