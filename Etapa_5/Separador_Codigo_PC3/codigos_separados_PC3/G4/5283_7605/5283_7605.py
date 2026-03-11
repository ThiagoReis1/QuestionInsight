n = int(input("Digite o numero: "))
i = 0
x = 0
while (n != 0):
		i = i + 1 
		if n > 0:
			x = x + 1
		n = int(input("Digite o numero: "))
print(i)
y = x/i * 100
print(round(y,2))
