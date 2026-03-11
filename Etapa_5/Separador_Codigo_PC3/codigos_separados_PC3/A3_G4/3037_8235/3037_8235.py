X = float(input("valor de x: "))
from math import*
fdex = X
if (X <= -1) or (X >= 1):
	fdex = X**2
if (-1 < X) and (X < 0) or (0 < X) and (X < 1):
	fdex = X
if (X==0):
	fdex = X = 1
print(round(fdex,4))

