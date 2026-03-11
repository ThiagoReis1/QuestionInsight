o = 15.999
c =12.011
n = 14.00674
h = 1.00794

nome_aminoacido = input().lower()

if (nome_aminoacido == "glutamina"):
	soma = (5*c) + (8*h) + n + (4*o)
	print(round(soma, 2))
elif (nome_aminoacido == "histidina"):
	soma = (6*c) + (10*h) + (3*n) + (2*o)
	print(round(soma, 2))
elif (nome_aminoacido == "prolina"):
	soma = (5*c) + (10*h) + n+ (o *2)
	print(round(soma, 2))
else:
	print("Entrada: ", nome_aminoacido)
	print("Dado Invalido")
	
