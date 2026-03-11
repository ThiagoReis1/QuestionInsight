from math import* 
b = float(input("lado b: "))
c = float(input("lado c: "))
alfa = radians(float(input("Ang alfa: ")))
a = (b**2+c**2-2*b*c*cos(alfa))**(1/2)
print(round(a,2))