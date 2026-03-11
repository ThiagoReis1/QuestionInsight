pesoSaco = float(input("Peso do saco de racao: "))
quant = float(input("Quantidade de racao: "))
resto = pesoSaco - (quant * 4)
print(round(resto, 2))