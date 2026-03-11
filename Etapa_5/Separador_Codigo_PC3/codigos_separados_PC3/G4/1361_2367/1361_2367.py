from math import *
x = int (input("Quantidade de porções: "))
sn = (sqrt(5)-1)/4
sf = (sqrt(5)-2*sqrt(5))
am = 5*(5-2*sqrt(5))
total = (sn+sf+am)* x
print (round(total,2))