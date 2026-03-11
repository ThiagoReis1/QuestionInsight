from numpy import * 
from math import *
vetP = array(eval(int(input("vetor: "))))
vetQ = array(eval(int(input("vetor: "))))
distancia = sqrt((vetP[0]-vetQ[0])**2 + (vetP[1]-vetQ[1])**2 + (vetP[-1]-vetQ[-1])**2)

sim = 1/(1+distancia)

print(round(distancia, 4))
print(round(sim, 2))
