from math import*
b= float(input())
c= float(input())
t= radians(float(input()))
a= (b*b+ c*c-2*b*c*cos(t))**(1/2)
print(round(a,2))