A = float(input("largura em metros: "))
a = float(input("comprimeto em metros: "))
b = float(input("custo por metro: "))
perimetro = 2*(A+a)
custo = perimetro * b
print(round(custo, 2))