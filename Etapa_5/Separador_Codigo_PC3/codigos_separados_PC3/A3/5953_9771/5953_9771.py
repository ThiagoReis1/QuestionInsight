lanche = 6
prato = 13.50
refrigerante = 3

t_ou_p = (input())
quant_prato_ou_lanche = int(input())
quant_refrigerante = int(input())

if t_ou_p == 'L':
	total = (quant_prato_ou_lanche  * 6) + (quant_refrigerante * 3)
	
	print(round(total, 2))
	
else:
	total = (quant_prato_ou_lanche * 13.5) + (quant_refrigerante * 3)
	
	print(round(total, 2))