from math import*
b = float(input("O lado b: "))
c = float(input("O lado c: "))
angulo = radians(float(input("O angulo a entre b e c (em graus): ")))


a = sqrt(b**2 + c**2 - 2 * b * c * cos(angulo))

print(round(a, 2))
