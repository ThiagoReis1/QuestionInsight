from math import *

# faça seu código aqui!
from math import *
lado = float(input("Qual o comprimento do lado do decagono? "))
vpi = pi/10
ang = tan(vpi)
apotema = (lado/(2*ang))
areadecagono = 5*lado*apotema
print(round(areadecagono, 2))

