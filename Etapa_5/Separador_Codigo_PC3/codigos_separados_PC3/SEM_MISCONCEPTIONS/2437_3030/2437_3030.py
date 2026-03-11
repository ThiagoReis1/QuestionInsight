preço_inicial = float(input("qual o preco da acao na abertura da bolsa?"))
preço_final = float(input("qual o preco da acao no fechamento da bolsa?"))

percentual = ((100 * preço_final) / preço_inicial) - 100

print(percentual)