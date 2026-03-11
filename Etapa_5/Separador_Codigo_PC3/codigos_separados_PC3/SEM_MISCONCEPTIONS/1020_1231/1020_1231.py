#Luiz Miguel Lira Antunes da Silva
#Prova 1; exercicio 1

B = float(input("Digite a base maior: "))
b = float(input("Digite a base menor: "))
h = float(input("Digite a altura: "))
custo = float(input("Digite o valor do custo: "))

area = h * (B + b)/2
total = area * custo

print(round(total, 2))