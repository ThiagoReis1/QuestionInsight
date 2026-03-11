consumo_energia = float(input("consumo de energia: "))
valor_conta = (0.43 * consumo_energia) + 10.00 
taxa = valor_conta * 25/100
custo_total = valor_conta + taxa
print(round(custo_total, 2))