valor = float(input("valro da compra"))
codigo = input("codigo D P ou C")

if codigo == "C":
	parcela = int(input("parcelas 1 ou 2"))
	if parcela ==2:
		valor=valor*1.07
else:
	valor = valor*0.88
print (valor)
