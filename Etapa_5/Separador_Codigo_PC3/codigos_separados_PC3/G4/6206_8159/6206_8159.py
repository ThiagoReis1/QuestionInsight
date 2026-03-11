n=float(input("Digite um numero: "))
cont=0
while n > -1:
	if 0 <= n <= 25:
		cont += 1
	n=float(input("Digite um numero: "))
print(cont)