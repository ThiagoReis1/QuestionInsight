estimativa = float(input("Estimativa da quantidade de acaizeiros: "))
comprimento = float(input("Comprimento da aresta do campo hexagonal: "))


a = (3*comprimento**2)**0.5
b = 3*(a/2)
c = int(b*estimativa)


print(c)