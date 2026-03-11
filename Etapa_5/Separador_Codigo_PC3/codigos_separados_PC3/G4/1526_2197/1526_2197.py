k = int(input("Digite valor de k: "))
p = int(input("Digite valor de p: "))
r = int(input("Digite valor de r: "))
cont = 0
acum = 0

while k > r:
	acum = acum + k * r
	cont = cont + acum / p
	cont = cont / 9
	cont = cont + 1
	print(acum)