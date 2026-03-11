num = int(input("Digite um numero: "))
x = 0

while (num != -1):
	if (num == 5):
		x = x + 1
		num = int(input("Digite um numero: "))
	else:
		if (num != 5):
			num = int(input("Digite um numero: "))
			
print(x)