escolha = input()
comida = int(input())
bebida = int(input())
total = comida * 5.00 + bebida * 12.00
if(escolha == "T"):
	total = total - comida * 0.50
print(round(total, 2))