from math import*
b = float(input("Informe o valor do lado b"))
c = float(input("Informe o valor do lado c"))
angulo = float(input("Informe o valor do angulo entre b e c"))
ang = radians(angulo)
a = ((b**2)+(c**2) - (2*b*c* (cos(ang)))) 
A = (float(sqrt(a)))
print(round(A,2))