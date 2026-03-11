import math

var = float(input("Digite estimativa de árvores por m²: "))
a = float(input("Digite o comprimento do lado da região da floresta: "))

area = int(a ** 2 * math.sqrt(25 + 10 * math.sqrt(5)) / 4)
qt_total_arvore = area * var

print(qt_total_arvore)