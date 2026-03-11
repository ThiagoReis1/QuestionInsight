gasto = float(input("Entre com o valor consumido: "))

consumo = gasto * 0.43 + 10 
total = consumo * (25/100) + consumo 


print(round(total, 2))