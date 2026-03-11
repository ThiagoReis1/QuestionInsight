a = float(input("lado1:"))
b = float(input("lado2:"))
c = float(input("lado3:"))
custo = float(input("custo:"))
perimetro = a + b + c

custo_total = perimetro * custo



print(round(custo_total, 2))