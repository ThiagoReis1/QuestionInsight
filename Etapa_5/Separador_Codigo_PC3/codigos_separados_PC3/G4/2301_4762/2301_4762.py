from math import*
b = (float(input("lado de b: ")))
c = (float(input("lado de c: ")))
A = radians(float(input("angulo alfa: ")))

a = (b**2)+(c**2)-(2*b*c)*(cos(A))
final = sqrt(a)

print(round(final,2))