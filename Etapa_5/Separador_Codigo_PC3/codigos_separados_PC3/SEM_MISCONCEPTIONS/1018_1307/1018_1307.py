# Problema: determinar custo por metro quadrado

# Variaveis

c1 = float(input("Digite o comprimento do cateto 1: "))
c2 = float(input("Digite o comprimento do cateto 2: "))

area = c1 * c2 / 2.0

custo = float(input("Insira o valor cobrado por metro quadrado: "))

total = custo * area

print(round(total,2))