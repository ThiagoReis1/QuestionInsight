N = int(input("Digite o valor de N: "))
acum = 1
cont = 0
inv = -1
div = 1
Sf = 0
while(cont != N):
	Sf = Sf + inv*((acum**0.5)/(9+div))
	inv = inv * (-1)
	acum = acum + 1
	div = div + 2
	cont = cont + 1
print(round(Sf, 6))