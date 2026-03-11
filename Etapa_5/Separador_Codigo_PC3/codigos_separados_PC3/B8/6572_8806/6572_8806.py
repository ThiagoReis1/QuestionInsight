# faça seu código aqui!

qnt = int(input("Informe a quantidade de pizzas que deseja comprar: "))

if(qnt < 3):
	valor = (qnt * 5) + 3
elif(qnt == 3):
	valor = (qnt * 5) + 3.25
elif(qnt > 3):
	valor = (qnt * 5) + 4.50
	
print("total= ", round(valor,2))