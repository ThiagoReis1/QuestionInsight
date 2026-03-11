from math import*
a=float(input("quantidade em metros:"))
b=float(input("custo da construcao em metros:"))
raio_a = 2*pi*a 
custo_total=raio_a*b
print(round(custo_total,2))