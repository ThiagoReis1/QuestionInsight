
af = int(input('Digite a area: '))

if(af<=10000):
	custo = af*5.00
else:
	dif = af - 10000
	custo = 10000*5.00 + dif*4.00

print(round(custo, 2))
	