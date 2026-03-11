preco = float(input("Valor total da compra: "))
formpag = input("Codigo de opcao de pagamento, [D]inheiro, [P]ix ou [C]artao?: ").upper()

if (formpag == "D") or (formpag == "P"):
	precofinal = preco * 0.81
	
elif (formpag == "C"):
	parcel = int(input("Parcelas, [1]x ou [2]x?: "))
	if parcel == 1:
		precofinal = preco * 1
	elif (parcel == 2):
		precofinal = preco + (preco * 0.09)
		
print(round(precofinal,2))
		
