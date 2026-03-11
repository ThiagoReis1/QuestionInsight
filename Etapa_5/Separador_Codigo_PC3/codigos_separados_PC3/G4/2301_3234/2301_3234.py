from math import*
b=(float(input("digite valor do lado b ")))
c=(float(input("digite valor do lado c ")))
a=radians(float(input("digite o angulo entre b e c ")))
#x=b**2+c**2-2*b*c*cos(a)
ladoA=sqrt(b**2+c**2-2*b*c*cos(a))
#print(x)
print(round(ladoA,2))