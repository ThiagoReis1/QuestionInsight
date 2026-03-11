num = int(input("Digite um numero: "))
count = 0
while (num != -1):
	if (num >= 76) and (num <= 100):
		count = count + 1
	num = int(input("Digite um numero: "))
print (count)