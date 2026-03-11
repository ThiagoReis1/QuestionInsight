# faça seu código aqui!
a = int(input("Digite a quantidade de dupla deliciosa: "))

if (a > 3):
	desconto = 0.2*32.90*a
	total = 32.90*a - desconto
	print(round(total,2))
else:
	total = 32.90*a
	print(round(total,2))