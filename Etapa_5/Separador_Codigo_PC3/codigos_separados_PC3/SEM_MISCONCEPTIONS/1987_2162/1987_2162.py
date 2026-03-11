nome = input("".upper())
if(nome == "ALANINA"):
	peso = 12.011*3+1.00794*7+14.00674+15.9994*2
	print(round(peso,2))
elif(nome == "VALINA"):
	peso2 = 12.011*5+1.00794*11+14.00674+15.9994*2
	print(round(peso2,2))
elif(nome == "TIROSINA"):
	peso3 = 12.011*9+1.00794*11+14.00674+15.9994*3
	print(round(peso3,2))
else:
	print("Entrada:", nome)
	print("Dado Invalido")