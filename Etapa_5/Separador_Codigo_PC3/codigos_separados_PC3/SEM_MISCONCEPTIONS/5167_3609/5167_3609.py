peso_racao = float(input("Peso saco:"))
quantidade_diaria = float(input("Quantidade diaria:"))

quantidade_semana = round(peso_racao - (quantidade_diaria*7),3)

print(quantidade_semana)