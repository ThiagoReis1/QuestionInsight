c = int(input("Digite o codigo do ninja:"))
s = float(input("Digite o salario atual do ninja:"))
c_101 = s + (s * 0.1)
c_102 = s + (s * 0.3)

if (c == 101):
	print(round(c_101, 2))
	print("Aumento de 10 por cento")
else:
	print(round(c_102, 2))
	print("Aumento de 30 por cento")