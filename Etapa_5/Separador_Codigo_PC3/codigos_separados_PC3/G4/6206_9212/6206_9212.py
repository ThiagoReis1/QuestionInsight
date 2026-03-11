num = int(input("digite um numero:"))
cont = 0

while num >= 0:
	if num >= 0 and num <= 25:
		cont = cont + 1
	num = int(input("digite um numero:"))
print(cont)