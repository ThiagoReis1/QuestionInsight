import math

b= float(input(""))
c= float(input(""))
a= math.radians(float(input("")))
alpha= math.sqrt((b ** 2)+(c ** 2)-2*b*c*math.cos(a))
print(round(alpha, 2))