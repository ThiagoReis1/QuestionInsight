num = int(input('Digite um valor entre 101 e 201: '))
cont = 0

while num != -1:
	if num >= 101 and num <= 201:
		cont = cont + 1
	num = int(input('Digite um valor entre 101 e 201: '))

print(cont)