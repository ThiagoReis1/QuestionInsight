abertura = float(input("preco da abertura: "))
fechamento = float(input("preco do fechamento: "))

dif =fechamento - abertura

percentual = (dif * 100 ) / abertura
print(round(percentual, 2))
