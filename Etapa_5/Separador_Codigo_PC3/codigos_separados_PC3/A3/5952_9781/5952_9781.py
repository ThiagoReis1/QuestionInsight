tapioca = 3.5
salgado = 5.0
acai = 13.0

T_ou_S = (input())
quant_tapioca_ou_salgado = int(input())
quant_acai = int(input())

if T_ou_S == 'T':
	total = (quant_tapioca_ou_salgado * 3.50 ) + (quant_acai * 13.0 )
	print(round(total, 2))
	
else:
	total = (quant_tapioca_ou_salgado * 5.0) + (quant_acai * 13.0 )
	print(round(total, 2))
	
 