x = int(input("Insira o Numero: "))
y = int(input("Insira o Numero: "))

nu = 0
i = x

while i <= y:
	if i % 5 == 0:
		nu = i
		print(nu)
	i = i + 1