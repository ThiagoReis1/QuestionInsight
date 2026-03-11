VI = float(input("Velocidade Inicial?: "))
DI = float(input("Distancia Falmer?: "))

import math

P1 = (DI * ( 9.8 / VI ** 2)) 
P2 = math.asin(P1) * (90 / math.pi)


print(round(P2, 2))