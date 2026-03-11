num = int(input("number: "))
cont = 0

while (num != -1):
	if (num >= 101) and (num <= 201):
		cont = cont + 1
	num = int(input("number: "))
print(cont)