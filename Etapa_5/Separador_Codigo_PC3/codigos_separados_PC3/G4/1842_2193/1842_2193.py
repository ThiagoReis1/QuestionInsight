from math import *
Qi = float(input("Qual o valor inicial: "))
Qf = float(input("Qual o valor final: "))
y = int(input("Numero de anos: "))
r = (log(Qf)-log(Qi))/y
print(float(r))