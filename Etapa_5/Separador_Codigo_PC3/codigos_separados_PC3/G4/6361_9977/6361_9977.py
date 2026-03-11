from numpy import*
a = int(input('Num: '))
b = 10
while a >= b:
	print(a)
	if a == b:
		print('Fim da contagem regressiva! ')
		a = a - 1
