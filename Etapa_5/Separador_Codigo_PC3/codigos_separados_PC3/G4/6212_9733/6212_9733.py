cont = 0
n = int(input("Digite o N:"))
while n != -1:
	if n >= 26 and n <= 85:
		cont = cont + 1
	n = int(input("numeros:"))
print(cont)