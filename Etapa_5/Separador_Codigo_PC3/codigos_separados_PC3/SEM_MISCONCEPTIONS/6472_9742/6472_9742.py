from math import *
lado = float(input("Qual o comprimento do lado? "))
apotema = lado/(2*tan(pi/9))
ae = (9*lado*apotema)/2
print(round(ae,2))