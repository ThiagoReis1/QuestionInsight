peso_saco = float(input("Peso: "))
quantidade_diaria = float(input("Quantidade: "))

quantidade_semana = quantidade_diaria*5
quantidade_restante = peso_saco - quantidade_semana
print(round(quantidade_restante,2))