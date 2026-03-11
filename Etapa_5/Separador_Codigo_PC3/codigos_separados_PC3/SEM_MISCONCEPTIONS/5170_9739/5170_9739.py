peso = float(input("Informe o peso total de racao: "))
quantidade = float(input("Informe a quantidade de racao diaria: "))

resto_da_racao = peso - 7 * quantidade

print(round(resto_da_racao, 3))