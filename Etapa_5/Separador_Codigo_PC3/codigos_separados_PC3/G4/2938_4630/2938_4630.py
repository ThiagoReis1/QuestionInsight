from math import*
x=float(input("distancia a: "))
y=float(input("distancia b: "))
z=radians(float(input("cos(): ")))
total=sqrt(x**2+y**2-(2*x*y*cos(z)))
print(round(total,2))