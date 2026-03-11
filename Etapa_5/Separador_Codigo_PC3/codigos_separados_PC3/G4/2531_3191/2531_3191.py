pre = float(input('Valor: '))
saq = float(input('Valor: '))
tx = float(input('Valor: '))
if pre > 0 and saq > 0 and tx > 0:
	p = pre*0.1 + pre
	t = 0
	saldo = pre
	s = saq
	while saldo <= p:
		saldo += saldo*tx 
		saldo = saldo - s
		saldo = round(saldo, 2)
		t += 1
	print(t)
else:
	print('Dados incorretos')
	