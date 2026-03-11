from math import *

# faça seu código aqui!

lado = float(input("Lado:"))

apo = lado/(2*(tan(pi/12)))
				
area = 6*lado*apo

print(round(area, 2))