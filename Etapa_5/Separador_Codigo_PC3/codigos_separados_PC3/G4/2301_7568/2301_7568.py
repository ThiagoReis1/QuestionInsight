import math
b= float(input(" b: "))
c = float(input("c: "))
y = math.radians(float(input(" y: ")))
m = (math.cos(y))
a = ((b**2)+(c**2) - 2*b*c*m)**(1/2)
print(round(a,2))