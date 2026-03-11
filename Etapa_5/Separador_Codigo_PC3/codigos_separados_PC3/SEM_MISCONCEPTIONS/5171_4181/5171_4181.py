
peso = float(input("Peso da racao: "))
quantidade = float(input("Quantidade diaria de racao: "))
dia = quantidade
semana = dia*7
resto = peso - semana
print(round(resto, 2))