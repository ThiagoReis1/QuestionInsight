from math import*

# faça seu código aqui!
a = float(input("o comprimento do lado do heptagono? "))
b = 2*tan(pi/7)
op = a/b
x = 3.5 * a * op
print(round(x,2))