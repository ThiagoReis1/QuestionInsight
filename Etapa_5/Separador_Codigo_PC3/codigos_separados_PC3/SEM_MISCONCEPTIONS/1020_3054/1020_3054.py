B = float(input("informe o valor: "))
b = float(input("informe o valor: "))
h = float(input("informe a altura: "))
servico = float(input("informe o valor: "))

area = h * (B + b) / 2

custo = area * servico

print(round(custo, 2))