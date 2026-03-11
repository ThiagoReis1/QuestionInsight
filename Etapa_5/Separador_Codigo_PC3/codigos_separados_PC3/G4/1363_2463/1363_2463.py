from math import*

p= float(input("Peso:"))

fr= 2**((1+p/1000))
sg= (p * pi**2)/3141
od= 2 * sqrt(p/40)

print(round(fr, 2))
print(round(sg, 2))
print(round(od, 2))
