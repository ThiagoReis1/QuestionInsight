from math import *
volume = float(input("Volume da agua consumida durante o mes: "))

a = 0.37 * volume
b = a + 15
c = b * 35/100
d = b + c


 
print(round(d,2))
