unidade=input().upper()
valor=float(input('valor: '))
if unidade == 'H':
	x= 2.47105*valor
if unidade == 'A':
	x=valor/2.47105
print(round(x,2))