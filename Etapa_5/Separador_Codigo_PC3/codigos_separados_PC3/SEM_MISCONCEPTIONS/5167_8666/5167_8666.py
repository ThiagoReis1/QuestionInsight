pesosacoracao=float(input("Digite o peso do saco de racao em gramas: "))
quantidadediariaracao=float(input("Digite  quantidade diária de racao em gramas: "))
quantidaderestante= pesosacoracao-(quantidadediariaracao*7)
print("A quantidade de racao restante apos uma semana e: ", round(quantidaderestante, 3))