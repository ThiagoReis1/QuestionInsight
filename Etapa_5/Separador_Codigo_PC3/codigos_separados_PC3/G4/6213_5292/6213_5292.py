num = int(input("digite um numero: "))
cont = 0

while (num != -1):
	if num >= 101  and num <= 201:
		cont = cont + 1
	num = int(input("digite outro numero: "))
print(cont)
	