peso = float(input("Digite o peso do saco de racao: "))
qtd = float(input("Digite a quantidade diaria: "))

total_semana = qtd * 7
resto = peso - total_semana
print(round(resto,2))