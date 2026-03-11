p1 = float(input("Digite o preco do primeiro jogo: "))
p2 = float(input("Digite o preco do segundo jogo: "))

totalp2 = p2 - (p2*(25/100))
totalcompra = p1 + totalp2

print(round(totalp2, 2))
print(round(totalcompra, 2))