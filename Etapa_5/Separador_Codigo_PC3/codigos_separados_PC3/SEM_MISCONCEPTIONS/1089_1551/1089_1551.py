valor1 = float(input("insira uma quantia: "))
valor2 = float(input("insira uma quantia: "))
valor3 = float(input("insira uma quantia: "))
limite = float(input("insira um limite: "))
total = valor1 + valor2 + valor3
if(total <= limite):
	print(round(total, 2))
	print("Sim")
else:
	print(round(total, 2))
	print("Nao")
	