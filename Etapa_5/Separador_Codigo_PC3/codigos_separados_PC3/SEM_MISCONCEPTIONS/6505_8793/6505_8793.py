# faça seu cód
var = input("Digite o tipo de entrada: ")
qtde = int(input("digite o valor: "))
valor = 30
total = valor * qtde

if( var == "C"):
	total = total - total * 15/100
	print(round(total,2))
else: 
	print(round(total,2))
  
