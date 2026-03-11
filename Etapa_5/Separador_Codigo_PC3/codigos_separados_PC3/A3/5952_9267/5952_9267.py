item = input("Tapioca: T ou Salgado: S").upper()
qtditem = int(input("qtditem: "))
qtdacai = int(input("qtdacai"))
valor = float(0)

if(item == "T"):
	valor = qtditem * 3.5 + qtdacai * 13
else:
	valor = qtditem * 5 + qtdacai * 13
print(round(valor,2))