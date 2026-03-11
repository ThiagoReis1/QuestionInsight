from math import*
e = float(input("estimativa de arvores por m2: "))
a = float(input("comprimento semieixo maior: "))
b = float(input("comprimento semieixo menor: "))
a = pi*a*b
p = a * e
print(round(p,0))
