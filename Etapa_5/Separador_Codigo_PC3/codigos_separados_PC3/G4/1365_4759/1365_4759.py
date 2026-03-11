from math import*
angulo= radians(float(input("qual o angulo: ")))
dist=float(input("qual a dist: "))
g= 9.8
v= g/sin(2*(angulo))
f= v*dist
h= sqrt(f)
print(round(h,2))