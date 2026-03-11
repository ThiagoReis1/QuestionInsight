#Lei dos cossenos

from math import*

b = float (input("Escreva o valor do lado b: "))
c = float(input("Escreva o valor do lado c: "))
angulo = radians(float (input("Escreva o valor do angulo entre b e c: ")))

a = b**2 + c**2 - 2*b*c*cos(angulo)
r = a**0.5

print(round(r,2))
