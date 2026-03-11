from math import*
r=float(input("raio::"))
l=int(input("lados:"))
a=1/2*(r*cos(pi/l))**2*(tan(pi/l))
print(round(a,2))