from math import *

# faça seu código aqui!

#Input
#-Lado do eneagono:
Lado = float(input("Lado: "))

#Calculos
#-Apotema:
Apotema = Lado/(2*(tan(pi/9)))
#Area:
Area = (9*Lado*Apotema)/2

#Print
print(round(Area,2))


