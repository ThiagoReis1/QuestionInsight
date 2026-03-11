#Peso do saco de ração (g) e Quantidade diária de ração (g)
peso = float(input("Digite o valor: "))
quantidade = float(input("Digite o valor: "))
#Cálculo quntidade de ração 
quantidade_de_racao = peso - (quantidade * 5)
#resultado
print(round(quantidade_de_racao, 2))
