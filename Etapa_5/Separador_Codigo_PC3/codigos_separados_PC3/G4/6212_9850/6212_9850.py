num = int(input("Digite um numero: "))

cont = 0

while num != -1:
	num = int(input("Digite um numero: "))
	if num >= 26 and num <= 85:
		cont = cont + 1
print(cont)