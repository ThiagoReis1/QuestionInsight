from math import*

b= float(input("digite o lado b:"))
c= float(input("digite o lado c:"))
ang=radians(float(input("digite o angulo entre b e c:")))

a=(b**2 + c**2 - 2*b*c*cos(ang))**0.5


print(round(a,2))
