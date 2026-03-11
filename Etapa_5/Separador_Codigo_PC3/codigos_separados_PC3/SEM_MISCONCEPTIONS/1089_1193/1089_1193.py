compra1 = float(input("primeira compra: "))
compra2 = float(input("segunda compra: "))
compra3 = float(input("terceira compra: "))
limite_cartao = float(input("limite: "))

preco = compra1 + compra2 + compra3
print(preco)
if (preco <= limite_cartao):
    print("Sim")
else:
    print("Nao")