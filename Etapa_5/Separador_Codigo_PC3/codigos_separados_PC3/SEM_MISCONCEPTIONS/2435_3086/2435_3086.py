x = float(input("digite o valor aqui: "))
frete = (5/100) * x
x_desconto = x - (x * (40/100))
print(round(x_desconto, 2))
print(round(frete, 2))
