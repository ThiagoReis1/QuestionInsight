num = 2
cont = 0
while num >= 0 :
	num = int(input('insira o numero: '))
	if num >= 26 and num <= 50:
		cont += 1
		
print(cont)