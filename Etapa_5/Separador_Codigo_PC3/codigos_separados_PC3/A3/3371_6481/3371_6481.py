unidade = input('K ou M').upper()
valor = float(input())

if unidade == 'K':
	conversao = valor/1.60934
if unidade == 'M':
	conversao = valor*1.60934
	
print(round(conversao, 2))