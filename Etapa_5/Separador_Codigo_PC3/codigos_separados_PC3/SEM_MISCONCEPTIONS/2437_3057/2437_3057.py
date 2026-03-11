#ENTRADA
preco_abertura = float(input("Preco de abertura: "))
preco_fechamento = float(input("Preco de fechamento: "))

#CALCULO
diferenca = preco_fechamento - preco_abertura
percentual = (diferenca * 100) / preco_abertura

#SAIDA
print(round(percentual,2))