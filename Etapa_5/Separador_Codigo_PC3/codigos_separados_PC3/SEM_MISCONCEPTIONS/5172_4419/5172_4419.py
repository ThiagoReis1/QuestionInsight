peso = float(input("Qual o peso(g) do saco de racao: "))
qtdDiaria = float(input("Qual a quantidade diaria de racao para cada porco somada: "))

qtdRestante = peso - (qtdDiaria * 5)

print(round(qtdRestante, 2))