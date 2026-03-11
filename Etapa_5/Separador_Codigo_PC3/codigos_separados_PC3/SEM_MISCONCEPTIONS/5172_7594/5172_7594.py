#entradas
peso = float(input("Peso do saco de racao (em gramas): "))
quantidade = float(input("Quantidade diaria em gramas: "))

#saidas
restante = peso - 5*quantidade
print(round(restante, 2))