from math import *
ladoEneagono = float(input("Digite o comprimento do lado do Eneagono:"))
apotema = (ladoEneagono / (2 * tan(pi / 9)))
areaEneagono = (9 * ladoEneagono * apotema) / 2
print(round(areaEneagono,2))