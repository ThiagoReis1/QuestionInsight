# Entradas
vs = float(input('Valor do sitio: '))
vi = float(input('Valor inicial depositado: '))
dm = float(input('Deposito mensal: '))
juros = float(input('Juros: '))

mes = 0  # contador

if vs > 0 and vi > 0 and dm > 0 and juros > 0:
	while vi < vs:
		vi = vi + (vi * juros/100)
		vi = vi + dm 
		mes = mes + 1
	if vi > vs:
		print(mes)
else:
	print('Dados incorretos')
		
		