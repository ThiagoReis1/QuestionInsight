escolha= input("L ou P:")
q1= int(input("Quantidade de lanches ou pratos executivos:"))
q2= int(input("Quantidade de refri:"))

if escolha == "L":
	print(float(q1 * 6 + q2 * 3))
else:
	print(float(q1 * 13.5 + q2 * 3))
	