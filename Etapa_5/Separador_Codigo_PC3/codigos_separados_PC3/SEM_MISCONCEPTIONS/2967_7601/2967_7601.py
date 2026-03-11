altura = float(input("Insira sua altura: "))
altura_a = float(input("Insira a altura do seu amigo: "))

x = altura_a or altura

if x >= 1.37:
	print("Sim")
	print(x)
else:
	print("Nao")
	if altura > altura_a:
		print(altura)
	if altura_a > altura:
		print(altura_a)	