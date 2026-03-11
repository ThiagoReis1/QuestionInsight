from math import*

Qz = float(input("Valor de Qz: "))

r = float(input("Valor de r entre 0,0 e 1,0: "))

y = (log(3*Qz) - log(Qz))/r

print(int(y + 1))