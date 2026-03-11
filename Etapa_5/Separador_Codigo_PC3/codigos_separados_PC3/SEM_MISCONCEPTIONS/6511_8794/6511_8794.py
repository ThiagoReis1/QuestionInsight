# faça seu código aqui!
var = input("Digite o tipo de entrada: ")
qtde = int(input("Digite o valor: "))
valor = 25.90

total = valor * qtde 

if(var == "B"):
	total = total - total * 10/100
	print(round(total,2))
else:
   print(round(total,2))