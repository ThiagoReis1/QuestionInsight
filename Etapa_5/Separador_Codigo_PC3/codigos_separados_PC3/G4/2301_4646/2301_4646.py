from math import*
b = float(input("lado b"))
c = float(input("lado c"))
a = radians(float (input("angulo")))
area = sqrt(b**2 + c**2 - 2*b*c * cos(a))
print(round(area,2))