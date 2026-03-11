n = int(input("digite um numero: "))
cont = 0

while n != -1:
	if 0 <= n<= 25:
		cont = cont + 1
	n = int(input("digite um numero: "))
print(cont)
