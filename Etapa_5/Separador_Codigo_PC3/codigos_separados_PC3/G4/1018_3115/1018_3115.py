a = float(input("Comprimento do 1 cateto:"))
b = float(input("Comprimento do 2 cateto:"))
c = float(input("Custo de aplicacao por metro quadrado:"))
area = a*b / 2
custo = area * c
print(round(custo,2))