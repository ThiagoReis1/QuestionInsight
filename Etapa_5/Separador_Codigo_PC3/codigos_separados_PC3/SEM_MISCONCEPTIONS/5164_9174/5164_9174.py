peso_saco = float(input("peso do saco: "))
quantidade_racao_diaria = float(input("quantidade racao: "))

Resto = peso_saco - (quantidade_racao_diaria * 4) 
print(round(Resto, 2))