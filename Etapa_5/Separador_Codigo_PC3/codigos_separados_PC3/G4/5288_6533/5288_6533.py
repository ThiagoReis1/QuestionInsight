n = int(input("Digite a idade: "))

cont = 0
cont2 = 0

while (n != -1):
	cont = cont + 1 
	if (n < 18):
		cont2 = cont2 + 1
	n = int(input("Digite a idade: "))
x = 100 * cont2 / cont
print(cont)
print(round(x, 2))
	


