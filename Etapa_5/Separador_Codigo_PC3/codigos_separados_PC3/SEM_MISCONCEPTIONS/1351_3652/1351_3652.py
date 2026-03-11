macas = float(input("Digite numero de macas por metro quadrado: "))
aresta = float(input("Digite o valor da aresta: "))

area = 3/2 * (3 * aresta ** 2) ** 0.5

total = macas * area

print(int(total))
