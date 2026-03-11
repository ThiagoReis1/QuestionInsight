from math import *

#valor inicial
qo = float(input())

#valor final
qf = float(input())

#anos
y = int(input())

#taxa de juros
r = (log(qf)-log(qo))/y

print(r)