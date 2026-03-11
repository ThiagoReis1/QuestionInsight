x = int(input("insira o ano: "))
y = input("insira a nacionalidade: (B/E/e/b)").upper()
a = 2023
if y == "E":
	idade = a - x 
	if idade >=18:
		print("sim")
		print(idade-18)
	else:
		print("nao")
		print(18-idade)
elif y == "B":
	idade = a - x
	if idade >= 21:
		print("sim")
		print(idade-21)
	else:
		print("nao")
		print(21-idade)
else:
	print("invalido")

