tip= input("Insira se voce comprou (C)Croissant ou (B)Bolo: ")
qnt= int(input("Qual a quantidade de bolo ou croissant adquiridos?: "))
cap= int(input("Qual a quantidade de capuccinos?: "))
if tip == "C":
	val= qnt*6.00 + cap*5.50
else:
	val= qnt*3.00 + cap*5.50

print(val)	