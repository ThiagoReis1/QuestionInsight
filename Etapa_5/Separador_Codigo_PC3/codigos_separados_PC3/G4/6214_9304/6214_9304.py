num = int(input("Numero: "))
i = 0

while (num != -1):
	if (num >= 45 and num <= 150):
		i = i +1
		num = int(input("Numero: "))
	else:
		num = int(input("Numero: "))
print(i)