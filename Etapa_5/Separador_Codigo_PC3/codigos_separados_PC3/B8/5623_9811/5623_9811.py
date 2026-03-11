bolo = 5.00
salgado = 4.00
cappuccino = 7.50

bolo_salgado = input("Bolo(B) ou Salgado(S):")
quantidadebs = int(input("digite a quantidade de bolo ou salgado:"))
quantidadecapp = int(input("digite a quantidade de cappuccino:"))


if bolo_salgado == "B":
	total = (quantidadebs * bolo) + (quantidadecapp * cappuccino)
	
elif bolo_salgado == "S":
	total = (quantidadebs * salgado) + (quantidadecapp * cappuccino)
	
print(round(total, 2))
