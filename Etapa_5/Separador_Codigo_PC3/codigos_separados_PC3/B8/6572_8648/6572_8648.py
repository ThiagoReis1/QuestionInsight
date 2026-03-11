#Variáveis de entrada:
numero_de_pizzas = int(input("Digite a quantidade de pizzas a ser encomendada: "))
#Cálculo e condições 
if (numero_de_pizzas < 3):
 total = numero_de_pizzas * 5.00 + 3.00
 print("total= ", round(total, ))
elif (numero_de_pizzas == 3):
 total = numero_de_pizzas * 5.00 + 3.25
 print("total= ", round(total, 2))
elif (numero_de_pizzas > 3):
 total = numero_de_pizzas * 5.00 + 4.50
 print("total= ", round(total, 2))
