# faça seu código aqui!
var1 = input("Dia da semana: ")
pratos = int(input("Quantidade de pratos: "))

if (var1 != "qua"):
	preco = pratos * 22
	print(round(preco , 2))
else:
	desc = (pratos * 22) * 15/100
	total2 = (pratos * 22) - desc
	print(round(total2,2))