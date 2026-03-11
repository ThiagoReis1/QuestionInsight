from math import *
x1=float(input("Comprimento do lado do pentagono: "))
apotema=x1/(2*(tan(pi/5)))
areapentagono=(5*x1*apotema)/2
print(round(areapentagono,2))