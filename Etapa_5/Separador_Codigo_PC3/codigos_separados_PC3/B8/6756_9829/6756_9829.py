# faça seu código aqui!
diaria = 175

dia = int(input("Quantidade de dias: "))

if dia < 15:
	print(round((dia*diaria) +20,2))
elif dia == 15:
	print(round((dia*diaria)+16, 2))
elif dia > 15:
	print(round((dia*diaria)+10 ,2))
	