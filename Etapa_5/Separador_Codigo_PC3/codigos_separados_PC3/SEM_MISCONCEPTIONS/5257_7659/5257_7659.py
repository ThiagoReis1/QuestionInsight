custo = float(input("digite o valor: "))

if ( custo <= 50.0):
	lucro = (custo * 100)/100
	total = custo + lucro
	print(round( total, 2))
if((custo >= 50.01) and ( custo <= 100.0)):
	lucro = (custo * 50)/100
	total = custo + lucro
	print(round(total, 2))
if ((custo >= 100.01) and (custo <=500.0)):
	lucro = (custo * 40)/100
	total =custo + lucro
	print(round(total, 2))
if ((custo > 500.01)):
	lucro = (custo * 30)/100
	total = custo + lucro
	print(round(total,2))
	