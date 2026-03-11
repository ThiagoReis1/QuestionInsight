
# faça seu código aqui!
var1 = float(input("Insira o comprimento do lado do heptagono: "))

# Calculos
from math import tan 
from math import pi

apotema = var1 / (2 * tan(pi/7))
area_hept = (7 * var1 * apotema) / 2

# Saida
print(round(area_hept , 2))
