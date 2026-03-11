vl = float(input("Valor da compra: "))
codigo = input("(D)Dinheiro:(P)Pix:(C)Credito: ")
total = vl

if codigo == "D":
	desconto = total - total * .18
elif codigo == "P":
	desconto = total - total * .18
elif codigo == "C":
	vezes = int(input("1 ou 2: "))
	if vezes == 1:
		desconto = vl
	else:
		desconto = total + total * .07
print(round(desconto, 2))
	
	
	
  