vt = float(input("Digite o valor total da compra: "))
co = input("'D' para dinheiro, 'P' para pix e 'C' para cartao: ").upper()

if (co == 'C'):
	pagamento = int(input("Digite '1' para uma vez e '2' para 2 vezes: "))
	
	if (pagamento == 1):
		total = vt
		print(round(total,2))
		
	else:
		total = (vt*0.06) + vt
		print(round(total,2))
		
elif (co == 'D' or co == 'P'):
	total = vt * (1-0.11)
	print(round(total,2))