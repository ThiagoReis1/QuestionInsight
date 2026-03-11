# Informações
peso_racao = float(input("Qual o peso do saco de racao?"))
quant_diaria = float(input("Qual a quantidade diara de racao?"))

# Cálculo do consumo de ração
resto = peso_racao - (quant_diaria *4)

# Saída
print(round(resto,2))