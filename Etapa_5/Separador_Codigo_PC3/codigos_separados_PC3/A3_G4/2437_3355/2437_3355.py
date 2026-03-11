a = float(input("Preco da acao inicial: "))
b = float(input("Preco da acao no fechamento da bolsa: "))


c = ((b-a)/a)*100
d = ((a-b)/a)*100

print(round(c, 1))