preco_abertura = float(input("Preco na abertura: "))
preco_fechamento = float(input("Preco no fechamento: "))

porcentagem = ((100 * preco_fechamento) / preco_abertura) - 100
print(porcentagem)