num=int(input("Entre com a qtde de pizzas: "))
fixo= 5.0

if (num < 3):
	cst= (num * fixo) + 3.0

elif (num == 3):
	cst= (num * fixo) + 3.25

else:
	cst= (num * fixo) + 4.50
	

print(round(cst,2))

