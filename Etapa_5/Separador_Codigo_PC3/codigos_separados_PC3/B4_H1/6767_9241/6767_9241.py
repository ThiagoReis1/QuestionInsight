valor= float(input("insira o valor total da compra: "))
codigo= input("digite (D) a vista, (P) pix (C1) cartao e (C2) cartao com juros: ")

if codigo == "D":
	total= valor - (valor * 12/100)
	print(round(total, 2))
elif codigo == "P":
	total= valor - (valor * 12/100)
	print(round(total, 2))
elif codigo == "C1":
	total= valor
	print(round(total, 2))
else:
	codigo == "C2"
	total= valor + (valor* 7/100)
	print(round(total, 2))
	
	
	33
	1