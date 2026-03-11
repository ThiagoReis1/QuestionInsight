num = int(input("Insira o Numero: "))

cont = 0

while num != -1:
	if num >= 51 and num <= 75:
		cont = cont + 1
	num = int(input("Insira o Numero: "))
print(cont)