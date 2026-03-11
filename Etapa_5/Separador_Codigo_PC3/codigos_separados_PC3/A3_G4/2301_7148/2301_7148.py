from math import*
b= float(input("lado ac:"))
c= float(input("lado ab:"))
a= float(input("lado cb:"))

a = sqrt(b**2)+(c**2)-2*b*c*cos(radians(alfa))
print (round(a, 2))