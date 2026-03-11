from math import*

ma= float(input("massa do caminhão A: "))
mb= float(input("massa do caminhão B: "))
vb= float(input("Velocidade de B:"))

vf= ((2*ma + mb)/(ma+mb)) * vb

print(vf)