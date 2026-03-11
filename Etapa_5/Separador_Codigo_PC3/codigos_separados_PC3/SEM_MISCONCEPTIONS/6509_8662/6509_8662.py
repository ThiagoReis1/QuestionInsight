hora = int(input('Digite o horario: '))
quant = int(input('Digite a quantidade: '))

total = 28.50 * quant 

if hora >= 18:
	total_a_pagar = total - total * 0.20
else:
	total_a_pagar = total
	
print(round(total_a_pagar, 2))