
from  math import *

# valor raio (a)
a = float(input("raio"))

# custo em metros
custo = float(input("custo: "))

# perimetro em metros
p = 2 * pi * a

# custo total
ct = p * custo

print(round(ct, 2))