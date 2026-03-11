from math import *

#valor investido (inicial)
q0 = float(input())

#anos
y = float(input())

#valor final
qf = float(input())

#juros
r = ((log(qf)-log(q0))/y)

print(round(r ,4)
		