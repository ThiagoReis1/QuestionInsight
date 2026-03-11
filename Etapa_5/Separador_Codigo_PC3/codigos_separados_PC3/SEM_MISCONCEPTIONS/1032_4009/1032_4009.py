encomenda = float(input("Digite o valor da encomenda: "))
correios = (81 / 100) * encomenda
total = (encomenda + correios) + 12

print(round(total, 2))