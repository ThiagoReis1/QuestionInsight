x = int(input("Digite o numero: "))

i = 0

while x != -1:
	if x >= 101 and x <= 201:
		i = i + 1
	x = int(input("Digite o numero: "))
print(i)