import math
b = float(input("digite o lado b: "))
c = float(input("digite o lado c: "))
ang = math.radians(float(input("digite o angulo entre b e c: ")))
a = math.sqrt(b**2+c**2-2*b*c*math.cos(ang))
print(round(a, 2))