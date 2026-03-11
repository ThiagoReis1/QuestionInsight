from math import*
peso = float(input("peso do saco: "))
qd = float(input("qd: "))
c = int(3)
d = int(4)
p1 = peso - (qd / c) * d 
print(round(p1, 2))