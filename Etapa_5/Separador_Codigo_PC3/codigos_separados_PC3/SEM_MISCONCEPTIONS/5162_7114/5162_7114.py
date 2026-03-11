var1 = float(input("Digite a estimativa de acaizeiros: "))

var2 = float(input("Digite o valor da aresta: "))


part1 = (3 * var2 ** 2) ** 0.5 / 2

formula = 3 * part1

print(int(formula * var1))