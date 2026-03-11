from math import*
comp = float(input("comp"))
custo = float(input("custo"))


area = (2*comp**2)* (2**0.5 +1)
cust_total = custo * area



print(round(cust_total,2))
