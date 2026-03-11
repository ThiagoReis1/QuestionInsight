from math import*

Qf=float(input("Qf: "))
r=float(input("r: "))
Q=Qf
y = int(log(Qf)-log(Q)/r)
print(y*3)
