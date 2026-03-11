from math import*
af=float(input("angulo da flexa?  "))
vi=float(input("velocidade inicial flezxa?  "))
d=(vi**2)*(sin(2*radians(af)))/9.8
print(round(d,2))