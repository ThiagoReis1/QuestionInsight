sb = float(input('valor total da compra: '))
cod = input('(D) dinheiro: (P) pix: (C) cartao: ').upper()
total = sb

if cod == 'D' or cod == 'P':
	total = sb - sb * 18/100
elif cod == 'C':
	par = int(input('em quantas parcelas? (1) ou (2): '))
	if par == 2:
		total = sb + sb * 7/100 
print(round(total, 2))