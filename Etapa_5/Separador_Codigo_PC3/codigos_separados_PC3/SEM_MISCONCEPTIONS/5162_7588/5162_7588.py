from math import *

numPerMeter = float(input())

aresta = float(input())

arestaSqrt = sqrt(3 * aresta **2)

areaHexag = 3 * (arestaSqrt/2)

prantasPerMeter = (numPerMeter) * (areaHexag)

print(int(prantasPerMeter))