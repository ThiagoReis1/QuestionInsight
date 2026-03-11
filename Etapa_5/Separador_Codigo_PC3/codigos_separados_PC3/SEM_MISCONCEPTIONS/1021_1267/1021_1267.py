#Ellen Barros de Almeida

from math import*

a = float(input("Digite o comprimento de a: "))

valor = float(input("Digite o valor por m2: "))

area = (3 * 3 ** 0.5 * a ** 2 / 2)

custo_total =  (area * valor)

print(round(custo_total, 2))