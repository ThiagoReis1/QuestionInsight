import math
Qo = float(input())
r = float(input())
y = int(( math.log(3*Qo) - math.log(Qo) ) / r) + 1
print(y)