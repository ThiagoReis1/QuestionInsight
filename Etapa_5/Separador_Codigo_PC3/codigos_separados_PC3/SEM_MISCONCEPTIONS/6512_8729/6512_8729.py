# faça seu código aqui!
dd = int(input("quantidade de duplas deliciosas: "))
valor = 32.90
desconto = 0.80
if(dd>3):
	x = (dd*valor*desconto)
	print(round(x,2))
else:
	y = (dd*valor)
	print(round(y,2))