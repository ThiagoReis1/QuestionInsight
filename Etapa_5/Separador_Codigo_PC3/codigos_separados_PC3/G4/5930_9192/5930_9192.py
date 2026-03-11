from math import*
p = float(input("valor da encomenda: "))

x = 81
y = 12

f = (p * (x/100)) + y
v = p + f
print(round(v,2))