from math import *

# faça seu código aqui!
lado= int(input("fornecer o lado: "))

apotema = lado/(2 * tan(pi/10))
areaD = 5 * lado * apotema 
print(round(areaD ,2))
