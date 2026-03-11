num = int(input("digite um numero e eu direi se ele eh magico: "))
cont = 0
while num != -1:
	if num >= 26 and num <= 50:
		cont = cont + 1
		num = int(input("digite outro numero e eu direi se ele eh magico: "))
	else:
		num = int(input("digite outro numero e eu direi se ele eh magico: "))
print(cont)