
pesoSaco = float(input("Peso saco: "))
qtdRacao = float(input("Quantidade de racao: "))


racaoRestantes = pesoSaco - qtdRacao * 5
print(round(racaoRestantes, 2))