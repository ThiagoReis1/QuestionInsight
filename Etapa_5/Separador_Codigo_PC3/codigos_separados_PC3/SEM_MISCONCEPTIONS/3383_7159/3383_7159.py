unidade = str(input())
valor = float(input())

if(unidade == 'K'):
	unid_conv = 2.20462 * valor
else:
	unid_conv = valor / 2.20462
	
print(round(unid_conv, 2))