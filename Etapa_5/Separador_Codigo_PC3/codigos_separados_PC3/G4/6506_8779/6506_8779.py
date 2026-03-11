# faça seu código aqui!
p = int(input("quantidade de pratos: "))
b = input("deseja sobremesa(s ou n)? ")
total = 40 * p
d = total - total * 5/100
if b == "s":
	print(round(d, 2))
else:
	print(round(total, 2))