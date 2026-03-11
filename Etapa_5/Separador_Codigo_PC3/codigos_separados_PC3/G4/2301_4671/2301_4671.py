import math

b=float(input("lado b: "))
c=float(input("lado c: "))
g=float(input("Angulo alfa: "))
g=math.radians(g)
a=float(math.sqrt((b**2)+(c**2)-2*b*c*math.cos(g)))

print(round(a,2))