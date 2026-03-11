X = input("Digite a medida: ")
y = float(input("Digite o valor: "))
mg = 2.35215*y
k = y/2.35215
if(X =='K'):
	print(round(mg,2))
if(X =='M'):
	print(round(k,2))
