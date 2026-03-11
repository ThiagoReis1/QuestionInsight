from math import *

Q0 = float(input("Valor inicial invesido: "))
R = float(input("taxa de rendimento: "))
Qf = Q0*3
y = (log(Qf)-log(Q0)) / R

print(int(y)+1)